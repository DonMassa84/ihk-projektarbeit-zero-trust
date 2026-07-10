from __future__ import annotations
import os, math, textwrap, hashlib
from pathlib import Path
from datetime import date
from xml.sax.saxutils import escape

from PIL import Image as PILImage, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image, KeepTogether, HRFlowable, Flowable, NextPageTemplate
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.utils import ImageReader

SCRIPT_DIR = Path(__file__).resolve().parent
OUT = SCRIPT_DIR.parent
ASSET = OUT / '08_assets' / 'v13'
ASSET.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR = OUT / '09_export' / 'reference_v13'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PDF_OUT = OUTPUT_DIR / 'PROJEKTARBEIT_ZERO_TRUST_IHK_V13_90_GATE.pdf'

# --------------------- fonts ---------------------
font_candidates = [
    ('LiberationSans', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
     '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
     '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'),
    ('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
     '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
     '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'),
]
for base, reg, bold, ital in font_candidates:
    if os.path.exists(reg):
        pdfmetrics.registerFont(TTFont(base, reg))
        pdfmetrics.registerFont(TTFont(base+'-Bold', bold))
        pdfmetrics.registerFont(TTFont(base+'-Italic', ital))
        FONT = base
        break
else:
    FONT = 'Helvetica'

NAVY = HexColor('#0B2B4C')
BLUE = HexColor('#1557A5')
LIGHT_BLUE = HexColor('#EAF2FB')
CYAN = HexColor('#1C8FC7')
GREEN = HexColor('#2E7D5A')
LIGHT_GREEN = HexColor('#E8F4EE')
ORANGE = HexColor('#C46A1A')
LIGHT_ORANGE = HexColor('#FFF1E5')
RED = HexColor('#B43C3C')
LIGHT_RED = HexColor('#FBECEC')
GRAY = HexColor('#5B6573')
LIGHT_GRAY = HexColor('#F3F5F7')
DARK = HexColor('#17202A')

# --------------------- generated image crop ---------------------
gen_img = ASSET / 'source_cover.png'
cover_crop = ASSET / 'cover_engine.png'
if gen_img.exists():
    im = PILImage.open(gen_img).convert('RGB')
    w,h = im.size
    crop = im.crop((12, 8, 330, 354))
    crop = crop.resize((1100, 1197), PILImage.Resampling.LANCZOS)
    crop.save(cover_crop, quality=95)

# --------------------- artifact helpers ---------------------
def save_fig(fig, name, dpi=180):
    p = ASSET / name
    fig.savefig(p, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return p

def artifact_swot():
    fig, ax = plt.subplots(figsize=(10,6.6)); ax.axis('off')
    boxes = [
        (0.03,0.52,0.45,0.42,'Stärken',['GitHub- und Automatisierungskenntnisse','Klare Pilotabgrenzung','Reproduzierbare Tests','Geringe Zusatzlizenzkosten'],'#E8F4EE','#2E7D5A'),
        (0.52,0.52,0.45,0.42,'Schwächen',['Begrenztes Stundenbudget','Kein vollständiges Enterprise-IAM','Pilotdaten statt Produktivmessung','Abhängigkeit von Schnittstellen'],'#FFF1E5','#C46A1A'),
        (0.03,0.04,0.45,0.42,'Chancen',['Standardisierte Rechteanträge','Bessere Nachvollziehbarkeit','Übertragbare Workflow-Bausteine','Basis für spätere IGA-Integration'],'#EAF2FB','#1557A5'),
        (0.52,0.04,0.45,0.42,'Risiken',['Unbelegte Kennzahlen','Berechtigungsfehler','Secret-Leakage','Scope Creep'],'#FBECEC','#B43C3C')]
    for x,y,w,h,t,items,fc,ec in boxes:
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=fc,edgecolor=ec,linewidth=1.8))
        ax.text(x+0.025,y+h-0.065,t,fontsize=14,weight='bold',color=ec,va='top')
        lines=[]
        for item in items:
            wrapped=textwrap.wrap(item,width=31) or [item]
            lines.append('• '+wrapped[0])
            lines.extend('  '+line for line in wrapped[1:])
        ax.text(x+0.032,y+h-0.145,'\n'.join(lines),fontsize=9.4,va='top',linespacing=1.25,color='#202830')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'01_swot.png')

def artifact_psp():
    fig, ax = plt.subplots(figsize=(11,6.5)); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.39,0.84),0.22,0.1,boxstyle='round,pad=.02',facecolor='#0B2B4C',edgecolor='none'))
    ax.text(0.5,0.89,'Zero-Trust-Pilot',ha='center',va='center',color='white',weight='bold',fontsize=15)
    phases = [
        ('1 Initiierung',['1.1 Auftrag','1.2 Ist-Analyse','1.3 Ziele'], '#DDEEFF'),
        ('2 Planung',['2.1 PSP/Zeit','2.2 Risiko','2.3 Kosten'], '#E8F4EE'),
        ('3 Konzeption',['3.1 RBAC','3.2 Architektur','3.3 Datenschutz'], '#FFF1E5'),
        ('4 Umsetzung',['4.1 Backend','4.2 Workflow','4.3 Audit'], '#F4EAFB'),
        ('5 Abschluss',['5.1 Tests','5.2 Übergabe','5.3 Doku'], '#FBECEC')]
    xs=[0.02,0.215,0.41,0.605,0.80]
    for (title,items,fc),x in zip(phases,xs):
        ax.add_patch(FancyBboxPatch((x,0.18),0.18,0.52,boxstyle='round,pad=.012',facecolor=fc,edgecolor='#8A98A8'))
        ax.add_patch(Rectangle((x,0.61),0.18,0.09,facecolor='#1557A5',edgecolor='none'))
        ax.text(x+0.09,0.655,title,ha='center',va='center',color='white',weight='bold',fontsize=10.5)
        for i,it in enumerate(items):
            yy=0.53-i*0.12
            ax.add_patch(FancyBboxPatch((x+0.02,yy-0.035),0.14,0.07,boxstyle='round,pad=.006',facecolor='white',edgecolor='#AAB5C0'))
            ax.text(x+0.09,yy,it,ha='center',va='center',fontsize=9.4)
        ax.add_patch(FancyArrowPatch((0.5,0.84),(x+0.09,0.70),arrowstyle='-|>',mutation_scale=12,color='#607080'))
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'02_psp.png')

def artifact_gantt():
    tasks=['Projektinitialisierung und Analyse','Konzept und Architekturdesign','Implementierung und GitHub-Integration','Test und Schulung','Projektabschluss und Übergabe']
    starts=[0,2,5,10,12]
    durations=[2,3,5,2,1]
    fig, ax=plt.subplots(figsize=(10,5.2))
    for i,(s,d) in enumerate(zip(starts,durations)):
        ax.barh(i,d,left=s,height=.55,color=plt.cm.Blues(0.38+0.07*i),edgecolor='#294B6B')
        ax.text(s+d/2,i,f'{[15,15,25,8,7][i]} h',ha='center',va='center',fontsize=9)
    ax.set_yticks(range(len(tasks)),tasks); ax.invert_yaxis(); ax.set_xlim(0,13)
    ax.set_xticks(range(0,14,2)); ax.set_xlabel('Projektwoche (13-Wochen-Rahmen laut Projektvorschlag, 70 aktive Prüfungsstunden)')
    ax.grid(axis='x',alpha=.25); ax.set_title('Zeitlicher Projektverlauf')
    return save_fig(fig,'03_gantt.png')

def artifact_stakeholder():
    fig,ax=plt.subplots(figsize=(8,6)); ax.set_xlim(0,5); ax.set_ylim(0,5)
    ax.axvline(2.5,color='#95A1AD'); ax.axhline(2.5,color='#95A1AD')
    ax.set_xlabel('Einfluss'); ax.set_ylabel('Interesse'); ax.set_xticks([0,2.5,5],['niedrig','mittel','hoch']); ax.set_yticks([0,2.5,5],['niedrig','mittel','hoch'])
    pts=[(4.5,4.6,'Auftraggeber'),(4.2,4.0,'IT-Administration'),(3.5,4.3,'Projektleiter'),(3.0,3.4,'Datenschutz'),(2.1,3.2,'Pilotnutzer'),(2.8,2.4,'Betriebsrat')]
    for x,y,l in pts:
        ax.scatter(x,y,s=180,color='#1557A5',edgecolor='white',zorder=3); ax.text(x+.08,y+.08,l,fontsize=10)
    ax.text(.15,4.75,'Informieren',weight='bold',color='#607080'); ax.text(3.5,4.75,'Eng einbinden',weight='bold',color='#1557A5')
    ax.text(.15,.15,'Beobachten',weight='bold',color='#607080'); ax.text(3.55,.15,'Zufrieden halten',weight='bold',color='#607080')
    ax.grid(alpha=.12)
    return save_fig(fig,'04_stakeholder.png')

def artifact_risk():
    labels=[('R1','Fehlberechtigung',3,5),('R2','Secret-Leakage',2,5),('R3','Scope Creep',4,3),('R4','Zeitverzug',3,3),('R5','Akzeptanz',3,2),('R6','Audit-Lücke',2,5)]
    fig,ax=plt.subplots(figsize=(9.8,6.4)); ax.set_xlim(.5,7.8); ax.set_ylim(.5,5.5)
    for x in range(1,6):
        for y in range(1,6):
            v=x*y
            c='#E8F4EE' if v<=5 else '#FFF1E5' if v<=12 else '#FBECEC'
            ax.add_patch(Rectangle((x-.5,y-.5),1,1,facecolor=c,edgecolor='white'))
            ax.text(x,y,str(v),ha='center',va='center',fontsize=8.5,color='#59636E')
    offsets={'R1':(.12,.12),'R2':(.12,-.20),'R3':(.12,.12),'R4':(.12,-.20),'R5':(.12,.12),'R6':(.12,.12)}
    for code,label,e,sev in labels:
        ax.scatter(e,sev,s=90,color='#0B2B4C',edgecolor='white',zorder=3)
        dx,dy=offsets[code]; ax.text(e+dx,sev+dy,code,fontsize=8.5,weight='bold')
    ax.set_xticks(range(1,6)); ax.set_yticks(range(1,6)); ax.set_xlabel('Eintrittswahrscheinlichkeit'); ax.set_ylabel('Schadensausmaß'); ax.set_title('Risikomatrix (Bewertung E x S)')
    ax.grid(False)
    ax.text(5.65,5.2,'Legende',fontsize=11,weight='bold',color='#0B2B4C')
    for i,(code,label,e,sev) in enumerate(labels):
        ax.text(5.65,4.75-i*.58,f'{code}: {label}',fontsize=9.2,va='center')
    return save_fig(fig,'05_risk.png')

def artifact_nutzwert():
    cats=['Kosten','Sicherheit','Automatisierung','Audit','Integration','Aufwand']
    manual=[5,2,1,1,2,5]; standard=[2,5,5,5,4,2]; pilot=[4,4,4,4,5,4]
    x=range(len(cats)); fig,ax=plt.subplots(figsize=(10,5.2))
    bw=.24
    ax.bar([i-bw for i in x],manual,width=bw,label='Manuell')
    ax.bar(x,standard,width=bw,label='Standard-IAM')
    ax.bar([i+bw for i in x],pilot,width=bw,label='GitHub-Pilot')
    ax.set_xticks(list(x),cats); ax.set_ylim(0,5.5); ax.set_ylabel('Bewertung 1-5'); ax.legend(ncol=3,loc='upper center'); ax.grid(axis='y',alpha=.2)
    ax.set_title('Nutzwertvergleich der Lösungsvarianten')
    return save_fig(fig,'06_nutzwert.png')

def artifact_architecture():
    fig,ax=plt.subplots(figsize=(11,6)); ax.axis('off')
    cols=[(0.03,'Nutzer',['Antragsteller','Genehmiger','Administrator']),(.25,'Portal',['React UI','Formular','Statusanzeige']),(.48,'Services',['FastAPI','Policy-Service','Audit-Service']),(.73,'Plattform',['GitHub API','PostgreSQL','Mail/Mock-IDP'])]
    for x,title,items in cols:
        ax.add_patch(FancyBboxPatch((x,.15),.2,.7,boxstyle='round,pad=.012',facecolor='#F8FAFC',edgecolor='#6C89A5',linewidth=1.3))
        ax.add_patch(Rectangle((x,.76),.2,.09,facecolor='#0B2B4C'))
        ax.text(x+.1,.805,title,ha='center',va='center',color='white',weight='bold')
        for i,it in enumerate(items):
            yy=.64-i*.17
            ax.add_patch(FancyBboxPatch((x+.025,yy-.045),.15,.09,boxstyle='round,pad=.006',facecolor='#EAF2FB',edgecolor='#8DB2D7'))
            ax.text(x+.1,yy,it,ha='center',va='center',fontsize=10)
    for x1,x2 in [(.23,.25),(.45,.48),(.68,.73)]:
        ax.add_patch(FancyArrowPatch((x1,.5),(x2,.5),arrowstyle='-|>',mutation_scale=16,color='#1557A5'))
    ax.text(.5,.06,'Pilotgrenze: keine Ablösung des zentralen Identity Providers, kein unternehmensweiter Produktivrollout',ha='center',fontsize=10,color='#B43C3C',weight='bold')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'07_architecture.png')

def artifact_workflow():
    fig,ax=plt.subplots(figsize=(10.5,5.4)); ax.axis('off')
    nodes=[('1 Antrag',.04),('2 Validierung',.22),('3 Genehmigung',.40),('4 Provisioning',.60),('5 Audit/Info',.80)]
    for t,x in nodes:
        ax.add_patch(FancyBboxPatch((x,.42),.15,.18,boxstyle='round,pad=.015',facecolor='#EAF2FB',edgecolor='#1557A5',linewidth=1.5))
        ax.text(x+.075,.51,t,ha='center',va='center',weight='bold',fontsize=10)
    for (_,x1),(_,x2) in zip(nodes,nodes[1:]):
        ax.add_patch(FancyArrowPatch((x1+.15,.51),(x2,.51),arrowstyle='-|>',mutation_scale=14,color='#0B2B4C'))
    ax.add_patch(FancyArrowPatch((.475,.42),(.475,.20),arrowstyle='-|>',mutation_scale=14,color='#B43C3C'))
    ax.add_patch(FancyBboxPatch((.37,.05),.21,.14,boxstyle='round,pad=.012',facecolor='#FBECEC',edgecolor='#B43C3C'))
    ax.text(.475,.12,'Ablehnung / keine Rechtevergabe',ha='center',va='center',fontsize=10)
    ax.text(.5,.82,'GitHub-basierter Rollenworkflow',ha='center',weight='bold',fontsize=16,color='#0B2B4C')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'08_workflow.png')

def artifact_erd():
    fig, ax = plt.subplots(figsize=(11.2, 7.4)); ax.axis('off')
    entities = {
        'BENUTZER': (.02,.67,.18,.24,['user_id (PK)','email','status']),
        'USER_ROLE': (.25,.67,.17,.24,['user_id (PK, FK)','role_id (PK, FK)','assigned_at']),
        'ROLLE': (.47,.67,.18,.24,['role_id (PK)','name','description']),
        'ROLE_PERMISSION': (.70,.67,.18,.24,['role_id (PK, FK)','permission_id (PK, FK)']),
        'BERECHTIGUNG': (.80,.34,.18,.24,['permission_id (PK)','resource','action']),
        'ROLLENANTRAG': (.02,.25,.20,.27,['request_id (PK)','user_id (FK)','requested_role_id (FK)','status','created_at']),
        'GENEHMIGUNG': (.30,.25,.19,.27,['approval_id (PK)','request_id (FK)','approver_id (FK)','decision','decided_at']),
        'AUDIT_EREIGNIS': (.57,.25,.20,.27,['event_id (PK)','request_id (FK)','actor_id (FK)','action','hash_prev','hash_curr']),
        'GITHUB_TEAM': (.80,.02,.18,.22,['team_id (PK)','team_slug','description']),
        'TEAM_ROLE': (.57,.02,.18,.22,['team_id (PK, FK)','role_id (PK, FK)'])
    }
    for name,(x,y,w,h,fields) in entities.items():
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.006',facecolor='white',edgecolor='#1557A5',linewidth=1.3))
        ax.add_patch(Rectangle((x,y+h-.055),w,.055,facecolor='#0B2B4C',edgecolor='none'))
        ax.text(x+w/2,y+h-.0275,name,ha='center',va='center',color='white',weight='bold',fontsize=8.6)
        for i,f in enumerate(fields):
            ax.text(x+.012,y+h-.083-i*.033,f,fontsize=7.5,va='top')
    def link(a,b,label,offset=(0,0)):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=9,color='#657789',linewidth=1.0))
        ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,fontsize=7.2,ha='center',bbox=dict(facecolor='white',edgecolor='none',pad=.5))
    link((.20,.79),(.25,.79),'1 : N')
    link((.42,.79),(.47,.79),'N : 1')
    link((.65,.79),(.70,.79),'1 : N')
    link((.88,.67),(.89,.58),'N : 1',(.035,0))
    link((.11,.67),(.11,.52),'1 : N',(.04,0))
    link((.22,.385),(.30,.385),'1 : 1')
    link((.49,.385),(.57,.385),'1 : N')
    link((.66,.25),(.66,.24),'1 : N')
    link((.75,.13),(.80,.13),'N : 1')
    link((.66,.24),(.56,.67),'N : 1',(-.02,.02))
    ax.text(.5,.955,'RBAC-Datenmodell des Piloten - normalisierte relationale Sicht',ha='center',fontsize=14.5,weight='bold',color='#0B2B4C')
    ax.text(.5,.925,'N:M-Beziehungen werden über Zuordnungstabellen modelliert; Genehmigungen und Audit-Ereignisse referenzieren den Rollen­antrag.',ha='center',fontsize=8.7,color='#5B6573')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'09_erd.png')

def artifact_audit():
    fig,ax=plt.subplots(figsize=(10.5,4.8)); ax.axis('off')
    events=['REQUEST','APPROVE','GRANT','NOTIFY']
    hashes=['a83f...','7c21...','dd90...','4f6a...']
    for i,(ev,h) in enumerate(zip(events,hashes)):
        x=.04+i*.24
        ax.add_patch(FancyBboxPatch((x,.38),.19,.27,boxstyle='round,pad=.012',facecolor='#F8FAFC',edgecolor='#1557A5'))
        ax.text(x+.095,.59,ev,ha='center',weight='bold',color='#0B2B4C')
        ax.text(x+.02,.51,'Hash: '+h,fontsize=9)
        ax.text(x+.02,.45,'Prev: '+('GENESIS' if i==0 else hashes[i-1]),fontsize=9)
        if i<3: ax.add_patch(FancyArrowPatch((x+.19,.515),(x+.24,.515),arrowstyle='-|>',mutation_scale=13,color='#2E7D5A'))
    ax.text(.5,.8,'Integritätsprüfung durch Hash-Verkettung (schematisch)',ha='center',fontsize=15,weight='bold',color='#0B2B4C')
    ax.text(.5,.17,'Beispieldaten: Eine Änderung wird bei der nächsten Integritätsprüfung erkennbar; dies ersetzt keine formale Revisionsprüfung.',ha='center',fontsize=10,color='#B43C3C')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'10_audit.png')

def artifact_tests():
    fig, ax = plt.subplots(figsize=(10,5.0))
    labels=['Testfälle definiert','Ergebnisstatus laut Unterlagen','Commit/Version zugeordnet','Laufzeit zugeordnet']
    values=[12,12,0,0]
    bars=ax.barh(labels,values,edgecolor='#294B6B')
    ax.set_xlim(0,12.8); ax.set_xticks(range(0,13,2)); ax.set_xlabel('Anzahl Testfälle')
    ax.set_title('Evidenzstatus des Pilot-Testlaufs')
    ax.grid(axis='x',alpha=.22)
    for bar,val in zip(bars,values):
        ax.text(val+.18,bar.get_y()+bar.get_height()/2,str(val),va='center',fontsize=10,weight='bold')
    ax.text(.02,-.22,'Bewertung: fachlicher Ergebnisstatus dokumentiert; reproduzierbarer Repository-Nachweis noch offen.',transform=ax.transAxes,fontsize=9.2,color='#B43C3C')
    fig.subplots_adjust(left=.28,bottom=.22)
    return save_fig(fig,'11_tests.png')

def artifact_cost():
    fig,ax=plt.subplots(figsize=(9.5,5.2))
    ax.bar(['Budgetrahmen'],[50000],width=.48,edgecolor='#294B6B')
    ax.set_ylim(0,56000); ax.set_ylabel('EUR'); ax.grid(axis='y',alpha=.22)
    ax.set_title('Budgetrahmen laut IHK-Projektvorschlag')
    ax.text(0,51200,'ca. 50.000 EUR',ha='center',va='bottom',fontsize=13,weight='bold',color='#0B2B4C')
    ax.text(0,39000,'Lizenzen\nSchulung\nexterne Beratung',ha='center',va='center',fontsize=11)
    ax.text(0,-6000,'Die 70 Prüfungsstunden des Teilnehmers sind nicht mit dem Gesamtprojektbudget gleichzusetzen.',ha='center',va='top',fontsize=9.5,color='#B43C3C')
    return save_fig(fig,'12_cost.png')

def artifact_rollout():
    fig,ax=plt.subplots(figsize=(10.5,4.8)); ax.axis('off')
    steps=[('Pilot','isolierte Testdaten\nbegrenzter Nutzerkreis'),('Stabilisierung','Fehlerbehebung\nBetriebsfreigabe'),('Fachbereich','begrenzter Rollout\nMonitoring'),('Skalierung','IGA/IDP-Integration\nRezertifizierung')]
    for i,(t,s) in enumerate(steps):
        x=.04+i*.24
        ax.add_patch(FancyBboxPatch((x,.30),.19,.30,boxstyle='round,pad=.012',facecolor=['#EAF2FB','#E8F4EE','#FFF1E5','#F4EAFB'][i],edgecolor='#687B8D'))
        ax.text(x+.095,.52,t,ha='center',weight='bold',fontsize=12)
        ax.text(x+.095,.40,s,ha='center',fontsize=9.5)
        if i<3: ax.add_patch(FancyArrowPatch((x+.19,.45),(x+.24,.45),arrowstyle='-|>',mutation_scale=14,color='#1557A5'))
    ax.text(.5,.78,'Einführungs- und Skalierungsroadmap',ha='center',fontsize=16,weight='bold',color='#0B2B4C')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'13_rollout.png')

def artifact_trace():
    fig,ax=plt.subplots(figsize=(10,5.4)); ax.axis('off')
    cols=[('Anforderung',['A01 RBAC','A02 Antrag','A03 Genehmigung','A04 GitHub','A05 Audit']),('Realisierung',['Rollenmatrix','React/FastAPI','Approval-Service','Actions/API','Hash-Log']),('Nachweis',['TF01/TF07','TF01/TF02','TF03/TF04','TF07','TF09/TF11'])]
    xs=[.05,.39,.73]
    for x,(title,rows) in zip(xs,cols):
        ax.add_patch(FancyBboxPatch((x,.12),.22,.70,boxstyle='round,pad=.012',facecolor='#F8FAFC',edgecolor='#1557A5'))
        ax.add_patch(Rectangle((x,.73),.22,.09,facecolor='#0B2B4C'))
        ax.text(x+.11,.775,title,ha='center',color='white',weight='bold')
        for i,r in enumerate(rows):
            y=.64-i*.11
            ax.add_patch(FancyBboxPatch((x+.02,y-.035),.18,.07,boxstyle='round,pad=.004',facecolor='white',edgecolor='#B0BBC6'))
            ax.text(x+.11,y,r,ha='center',va='center',fontsize=9)
    for i in range(5):
        y=.64-i*.11
        ax.add_patch(FancyArrowPatch((.27,y),(.39,y),arrowstyle='-|>',mutation_scale=11,color='#607080'))
        ax.add_patch(FancyArrowPatch((.61,y),(.73,y),arrowstyle='-|>',mutation_scale=11,color='#607080'))
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    return save_fig(fig,'14_traceability.png')

ARTIFACTS = [artifact_swot(), artifact_psp(), artifact_gantt(), artifact_stakeholder(), artifact_risk(), artifact_nutzwert(), artifact_architecture(), artifact_workflow(), artifact_erd(), artifact_audit(), artifact_tests(), artifact_cost(), artifact_rollout(), artifact_trace()]

# --------------------- ReportLab document ---------------------
PAGE_W, PAGE_H = A4
LEFT=15*mm; RIGHT=45*mm; TOP=25*mm; BOTTOM=25*mm
CONTENT_W = PAGE_W - LEFT - RIGHT

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyX',fontName=FONT,fontSize=12,leading=18,textColor=DARK,spaceAfter=5.5,alignment=TA_LEFT,widowOrphanControl=1))
styles.add(ParagraphStyle(name='BodySmall',fontName=FONT,fontSize=10,leading=14,textColor=DARK,spaceAfter=4))
styles.add(ParagraphStyle(name='H1X',fontName=FONT+'-Bold',fontSize=18,leading=22,textColor=NAVY,spaceBefore=8,spaceAfter=10,keepWithNext=1))
styles.add(ParagraphStyle(name='H2X',fontName=FONT+'-Bold',fontSize=14,leading=18,textColor=BLUE,spaceBefore=8,spaceAfter=6,keepWithNext=1))
styles.add(ParagraphStyle(name='H3X',fontName=FONT+'-Bold',fontSize=12.5,leading=16,textColor=DARK,spaceBefore=6,spaceAfter=4,keepWithNext=1))
styles.add(ParagraphStyle(name='CaptionX',fontName=FONT+'-Italic',fontSize=8.8,leading=11,textColor=GRAY,alignment=TA_CENTER,spaceBefore=3,spaceAfter=8))
styles.add(ParagraphStyle(name='TableCaptionX',fontName=FONT+'-Italic',fontSize=8.8,leading=11,textColor=GRAY,alignment=TA_LEFT,spaceBefore=3,spaceAfter=4))
styles.add(ParagraphStyle(name='BulletX',fontName=FONT,fontSize=11.5,leading=17,leftIndent=14,firstLineIndent=-8,bulletIndent=5,spaceAfter=3))
styles.add(ParagraphStyle(name='CalloutX',fontName=FONT,fontSize=10.5,leading=15,textColor=NAVY,leftIndent=8,rightIndent=8,spaceBefore=6,spaceAfter=6,borderWidth=0.7,borderColor=HexColor('#9BB8D3'),borderPadding=7,backColor=LIGHT_BLUE))
styles.add(ParagraphStyle(name='RiskCallout',fontName=FONT,fontSize=10.3,leading=14.8,textColor=RED,leftIndent=8,rightIndent=8,spaceBefore=6,spaceAfter=6,borderWidth=0.7,borderColor=RED,borderPadding=7,backColor=LIGHT_RED))
styles.add(ParagraphStyle(name='TitleBig',fontName=FONT+'-Bold',fontSize=24,leading=28,textColor=NAVY,alignment=TA_LEFT,spaceAfter=8))
styles.add(ParagraphStyle(name='TitleSub',fontName=FONT,fontSize=12.5,leading=17,textColor=DARK,spaceAfter=12))
styles.add(ParagraphStyle(name='FrontH',fontName=FONT+'-Bold',fontSize=18,leading=22,textColor=NAVY,spaceAfter=12))
styles.add(ParagraphStyle(name='TOC1X',fontName=FONT,fontSize=10.5,leading=15,leftIndent=0,firstLineIndent=0,textColor=DARK))
styles.add(ParagraphStyle(name='TOC2X',fontName=FONT,fontSize=9.5,leading=13.2,leftIndent=12,firstLineIndent=0,textColor=GRAY))

class MainStartMarker(Flowable):
    def __init__(self): super().__init__(); self.width=0; self.height=0
    def draw(self): self._doctemplate.main_start_page=self.canv.getPageNumber()

class FigureEntry(Flowable):
    def __init__(self, label, kind='figure'):
        super().__init__(); self.label=label; self.kind=kind; self.width=0; self.height=0
    def draw(self):
        doc=self._doctemplate
        if not doc.main_start_page:
            return
        page_num=self.canv.getPageNumber()-doc.main_start_page+1
        key=f'{self.kind}-{hashlib.md5(self.label.encode()).hexdigest()[:10]}'
        self.canv.bookmarkPage(key)
        notify_kind='FIGEntry' if self.kind=='figure' else 'TABEntry'
        doc.notify(notify_kind,(0,self.label,page_num,key))

class IHKDocTemplate(BaseDocTemplate):
    def beforeDocument(self):
        self.main_start_page=None
        self.figure_entries=[]

    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        self.main_start_page=None
        self.figure_entries=[]
        frame=Frame(LEFT,BOTTOM,PAGE_W-LEFT-RIGHT,PAGE_H-TOP-BOTTOM,id='normal',leftPadding=0,rightPadding=0,topPadding=8,bottomPadding=0)
        cover_frame=Frame(0,0,PAGE_W,PAGE_H,id='cover',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='Cover',frames=[cover_frame],onPage=self.cover_page),
            PageTemplate(id='Normal',frames=[frame],onPage=self.header_page,onPageEnd=self.footer_page),
        ])
    def cover_page(self,canvas,doc):
        canvas.saveState(); canvas.setFillColor(colors.white); canvas.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0); canvas.restoreState()
    def header_page(self,canvas,doc):
        canvas.saveState()
        canvas.setFont(FONT,8.5); canvas.setFillColor(GRAY)
        canvas.drawString(LEFT,PAGE_H-12*mm,'Zero-Trust-Sicherheitskonzept mit GitHub-Integration')
        canvas.drawRightString(PAGE_W-RIGHT,PAGE_H-12*mm,'Stand: 01.11.2026')
        canvas.setStrokeColor(HexColor('#AAB5C0')); canvas.setLineWidth(.5); canvas.line(LEFT,PAGE_H-14*mm,PAGE_W-RIGHT,PAGE_H-14*mm)
        canvas.restoreState()
    def footer_page(self,canvas,doc):
        p=canvas.getPageNumber()
        if p==1: return
        canvas.saveState(); canvas.setStrokeColor(HexColor('#AAB5C0')); canvas.setLineWidth(.5); canvas.line(LEFT,14*mm,PAGE_W-RIGHT,14*mm)
        canvas.setFont(FONT,8.5); canvas.setFillColor(GRAY); canvas.drawString(LEFT,9.5*mm,'Daniel Massa')
        if self.main_start_page and p>=self.main_start_page:
            num=str(p-self.main_start_page+1)
        else:
            num=roman(max(1,p-1)).lower()
        canvas.drawRightString(PAGE_W-RIGHT,9.5*mm,num); canvas.restoreState()
    def afterFlowable(self,flowable):
        if isinstance(flowable, Paragraph):
            style=flowable.style.name
            if style in ('H1X','H2X','H3X'):
                level={'H1X':0,'H2X':1,'H3X':2}[style]
                text=flowable.getPlainText()
                key='h%d-%s'%(level,hashlib.md5(text.encode()).hexdigest()[:8])
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text,key,level=level,closed=False)
                
                toc_page = self.page
                if self.main_start_page and self.page >= self.main_start_page:
                    toc_page = self.page - self.main_start_page + 1
                self.notify('TOCEntry',(level,text,toc_page,key))

def roman(n):
    vals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    s=''
    for v,r in vals:
        while n>=v: s+=r; n-=v
    return s

story=[]
fig_no=0; table_no=0

def P(text,style='BodyX'): story.append(Paragraph(text,styles[style]))
def H1(text): story.append(Paragraph(text,styles['H1X']))
def H2(text): story.append(Paragraph(text,styles['H2X']))
def H3(text): story.append(Paragraph(text,styles['H3X']))
def bullets(items):
    for it in items: story.append(Paragraph('• '+it,styles['BulletX']))
def callout(text,risk=False): story.append(Paragraph(text,styles['RiskCallout' if risk else 'CalloutX']))
def fig(path,caption,width=155*mm,maxh=150*mm):
    global fig_no
    fig_no += 1
    im=PILImage.open(path); w,h=im.size
    width=min(width, CONTENT_W)
    scale=min(width/w,maxh/h)
    rw, rh=w*scale,h*scale
    story.append(KeepTogether([Image(str(path),width=rw,height=rh),FigureEntry(f'Abbildung {fig_no}: {caption}','figure'),Paragraph(f'Abbildung {fig_no}: {caption}',styles['CaptionX'])]))
    return fig_no

def _table_cell(value, font_size, header=False):
    if isinstance(value, (Paragraph, Image, Flowable)):
        return value
    txt = escape(str(value)).replace('\n','<br/>')
    style = ParagraphStyle(
        name=f'TCell_{font_size}_{"H" if header else "B"}',
        fontName=FONT+'-Bold' if header else FONT,
        fontSize=font_size,
        leading=font_size+2.2,
        textColor=colors.white if header else DARK,
        alignment=TA_LEFT,
        wordWrap='CJK',
        splitLongWords=1,
        spaceAfter=0,
        spaceBefore=0,
        allowWidows=0,
        allowOrphans=0,
    )
    return Paragraph(txt, style)

def tab(data,caption,widths=None,repeat=1,font=8.7,numbered=True):
    global table_no
    if numbered:
        table_no += 1
        story.append(FigureEntry(f'Tabelle {table_no}: {caption}','table'))
        story.append(Paragraph(f'Tabelle {table_no}: {caption}',styles['TableCaptionX']))
    wrapped=[]
    for r,row in enumerate(data):
        wrapped.append([_table_cell(v,font,header=(r==0)) for v in row])
    if widths:
        total = float(sum(widths))
        if total > CONTENT_W:
            factor = CONTENT_W / total
            widths = [w * factor for w in widths]
    else:
        ncols = max(len(row) for row in data)
        widths = [CONTENT_W / ncols] * ncols
    t=Table(wrapped,colWidths=widths,repeatRows=repeat,hAlign='LEFT',splitByRow=1)
    ts=[
        ('BACKGROUND',(0,0),(-1,0),NAVY),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('GRID',(0,0),(-1,-1),.35,HexColor('#B7C0C9')),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT_GRAY]),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
        ('TOPPADDING',(0,0),(-1,-1),3.5),('BOTTOMPADDING',(0,0),(-1,-1),3.5),
    ]
    t.setStyle(TableStyle(ts)); story.append(t); story.append(Spacer(1,5))
    return table_no if numbered else None


# Cover
story.append(NextPageTemplate('Cover'))
cover_items=[]
cover_items.append(Spacer(1,12*mm))
cover_items.append(Paragraph('IHK REGION STUTTGART',ParagraphStyle(name='CoverIHK',fontName=FONT+'-Bold',fontSize=18,leading=22,textColor=NAVY,alignment=TA_CENTER,spaceAfter=8)))
cover_items.append(HRFlowable(width='100%',thickness=1.2,color=BLUE,spaceBefore=2,spaceAfter=12))
cover_items.append(Paragraph('Projektdokumentation',ParagraphStyle(name='CoverDoc',fontName=FONT+'-Bold',fontSize=22,leading=26,textColor=DARK,alignment=TA_CENTER,spaceAfter=8)))
cover_items.append(Paragraph('Betrieblicher IT-Prozess',ParagraphStyle(name='CoverProc',fontName=FONT+'-Bold',fontSize=15,leading=19,textColor=BLUE,alignment=TA_CENTER,spaceAfter=12)))
cover_items.append(Paragraph('Einführung eines Zero-Trust-Sicherheitskonzepts mit automatisierter Rechtevergabe und GitHub-basierter Workflow-Integration',ParagraphStyle(name='CoverTitle',fontName=FONT+'-Bold',fontSize=20,leading=24,textColor=NAVY,alignment=TA_CENTER,spaceAfter=12)))
if cover_crop.exists():
    cover_items.append(Image(str(cover_crop),width=136*mm,height=64*mm))
    cover_items.append(Spacer(1,4*mm))
cover_items.append(Paragraph('Im Rahmen der Fortbildungsprüfung 2026 zum<br/><b>Certified IT Business Manager</b>',ParagraphStyle(name='CoverTrain',fontName=FONT,fontSize=13,leading=18,textColor=DARK,alignment=TA_CENTER,spaceAfter=10)))
cover_data=[
    ['Prüfungsteilnehmer','Daniel Massa'],
    ['Anschrift','Hackstraße 41, 70190 Stuttgart'],
    ['Telefon','+49 178 2989360'],
    ['E-Mail','Massa.Daniel@proton.me'],
    ['Prüflingsnummer','615951'],
    ['Praktikumsbetrieb','Verein zur Förderung der Berufsbildung e. V., Kurfürstenstraße 6, 71636 Ludwigsburg'],
    ['Projektumfeld','IT-Projektmanagement / IT-Sicherheit / digitale Verwaltung / Zugriffskontrolle'],
    ['Projektcoach','Carsten Vordermeier'],
    ['Kontakt Projektcoach','07136 396663 / vordermeier@c-tim.de'],
    ['Zuständige IHK','IHK Region Stuttgart'],
    ['Abgabedatum','01.11.2026'],
]
cover_table=Table([[Paragraph('<b>'+escape(a)+'</b>',styles['BodySmall']),Paragraph(escape(b),styles['BodySmall'])] for a,b in cover_data],colWidths=[50*mm,103*mm],hAlign='CENTER')
cover_table.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.35,HexColor('#B7C0C9')),('BACKGROUND',(0,0),(0,-1),LIGHT_BLUE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
cover_items.append(cover_table)
cover_outer=Table([[cover_items]],colWidths=[PAGE_W],rowHeights=[PAGE_H])
cover_outer.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),18*mm),('RIGHTPADDING',(0,0),(-1,-1),18*mm),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(cover_outer)
story.append(NextPageTemplate('Normal')); story.append(PageBreak())

# Sperrvermerk
P('Sperrvermerk','FrontH')
P('Die vorliegende Projektarbeit enthält projektbezogene Informationen aus dem Projekt-/Praktikumsbetrieb Verein zur Förderung der Berufsbildung e. V. Eine Weitergabe außerhalb des Prüfungs- und Freigabeprozesses ist nur mit Zustimmung des Verfassers und des beteiligten Projektbetriebs zulässig.')
story.append(PageBreak())

P('Management Summary und Projektüberblick','FrontH')
P('Das im IHK-Projektvorschlag beschriebene Vorhaben dient der Entwicklung eines Zero-Trust-Sicherheitsmodells inklusive automatisierter Zugriffs- und Rechtevergabe. Daniel Massa übernimmt die Rolle des Projektleiters und verantwortet die Analyse der bestehenden IT-Sicherheitsarchitektur, die Konzeption des Zero-Trust-Ansatzes, den Aufbau einer automatisierten RBAC-Rechtevergabe über GitHub-Workflows, Audit-Logs und Compliance-Nachweise sowie Test, Schulung, Abnahme und Übergabe. Im technischen Pilot stehen ein strukturierter Self-Service-Antrag, eine nachvollziehbare Genehmigung, die automatisierte Zuordnung zu GitHub-Teams und eine manipulationserschwerende Audit-Protokollierung im Mittelpunkt. GitHub wird dabei als Workflow- und Integrationsplattform eingesetzt, nicht als vollständiger Ersatz eines unternehmensweiten Identity-and-Access-Management-Systems.')
P('Der IHK-Projektvorschlag sieht fünf Projektphasen mit insgesamt 13 Wochen vor. Die 70 aktiven Stunden bezeichnen ausschließlich den dokumentierten Prüfungsaufwand des Prüfungsteilnehmers und nicht den Gesamtaufwand des betrieblichen Projekts. Der Pilot verwendet isolierte Testdaten und begrenzt sich auf ausgewählte Rollen und Repositories. Produktive Migrationen, unternehmensweite Rezertifizierung, privilegiertes Zugriffsmanagement und die Ablösung eines zentralen Identity Providers sind ausdrücklich ausgeschlossen.')
P('Die technische Pilotlösung besteht aus einem React-basierten Frontend, einem FastAPI-Backend, PostgreSQL für Rollen- und Auditdaten sowie GitHub Actions beziehungsweise GitHub API für die Workflow-Automatisierung. Zwölf in den Projektunterlagen definierte Testfälle bilden den dokumentierten fachlichen Ergebnisstand; ein automatisierter Repository-Testreport ist vor der Abgabe noch eindeutig zuzuordnen und gegen den Mindeststandard aus Kapitel 6.6 zu prüfen. Der Projektvorschlag nennt einen Budgetrahmen von ca. 50.000 EUR für Lizenzen, Schulung und externe Beratung.')
callout('Kanonischer Technikstand dieser Fassung: Python/FastAPI. Abweichende Node.js-/Express- oder pauschale ROI-Fassungen sind nicht Bestandteil dieses Abgabekandidaten.')
callout('<b>Ergebnis:</b> Die Dokumentation folgt der IHK-orientierten Projektlogik Projektauftrag - Planung - Spezifikation - Durchführung - Test - Abschluss. Die persönliche Projektleiterleistung, Entscheidungswege, Controlling-Instrumente und technischen Nachweise sind durchgängig sichtbar.')
story.append(PageBreak())

# TOC
P('Inhaltsverzeichnis','FrontH')
toc=TableOfContents(); toc.levelStyles=[styles['TOC1X'],styles['TOC2X'],ParagraphStyle(name='toc3',parent=styles['TOC2X'],leftIndent=24,fontSize=8.8)]
story.append(toc); story.append(PageBreak())

P('Abbildungs- und Tabellenverzeichnis','FrontH')
P('Die Verzeichnisse werden beim Mehrfach-Build automatisch aus den tatsächlichen Bild- und Tabellenunterschriften einschließlich ihrer Hauptteil-Seitenzahlen erzeugt.')
P('<b>Abbildungsverzeichnis</b>','BodyX')
fig_toc=TableOfContents(notifyKind='FIGEntry',dotsMinLevel=0)
fig_toc.levelStyles=[ParagraphStyle(name='FigIndex',parent=styles['TOC1X'],fontSize=9.2,leading=12.5,leftIndent=0)]
story.append(fig_toc)
story.append(Spacer(1,5*mm))
P('<b>Tabellenverzeichnis</b>','BodyX')
tab_toc=TableOfContents(notifyKind='TABEntry',dotsMinLevel=0)
tab_toc.levelStyles=[ParagraphStyle(name='TabIndex',parent=styles['TOC1X'],fontSize=8.7,leading=11.8,leftIndent=0)]
story.append(tab_toc)
story.append(PageBreak())

P('Abkürzungsverzeichnis' ,'FrontH')
abbr=[['Abkürzung','Bedeutung'],['API','Application Programming Interface'],['CI/CD','Continuous Integration / Continuous Delivery'],['DSGVO','Datenschutz-Grundverordnung'],['IAM','Identity and Access Management'],['IGA','Identity Governance and Administration'],['IDP','Identity Provider'],['MFA','Multi-Faktor-Authentifizierung'],['NIST','National Institute of Standards and Technology'],['OPA','Open Policy Agent'],['RBAC','Role-Based Access Control'],['REST','Representational State Transfer'],['SSO','Single Sign-On'],['TOM','Technische und organisatorische Maßnahmen'],['UAT','User Acceptance Test']]
tab(abbr,'Abkürzungen',widths=[38*mm,112*mm],font=9.2,numbered=False)
story.append(PageBreak())

# Main start
story.append(MainStartMarker())
H1('1 Projektinformationen und Initiierung')
H2('1.1 Projektumfeld und Ausgangslage')
P('Die Projektarbeit behandelt einen sicherheitsorientierten Berechtigungsprozess beim Verein zur Förderung der Berufsbildung e. V. im Projektumfeld IT-Projektmanagement, IT-Sicherheit, digitale Verwaltung und Zugriffskontrolle. Der Projektvorschlag adressiert die bestehende IT-Sicherheitsarchitektur und die GitHub-basierte Automatisierung von Rollen- und Rechtevergaben. Berechtigungsänderungen wurden bislang überwiegend über unstrukturierte Kommunikationswege angestoßen. Dadurch entstehen Medienbrüche, uneinheitliche Freigaben und ein erhöhter Aufwand bei der späteren Nachvollziehbarkeit.')
P('Die im Ausgangsdokument genannten Mengen- und Fehlerwerte werden in dieser Fassung nicht als ungeprüfte Unternehmenskennzahlen übernommen. Für die Kostenplanung wird der im IHK-Projektvorschlag bestätigte Budgetrahmen verwendet. Produktivwerte und tatsächliche Kosten dürfen erst nach einer dokumentierten Stichprobe, Zeiterfassung oder Belegauswertung als Ist-Werte bezeichnet werden.')
H2('1.2 Problemstellung')
P('Ein Berechtigungsprozess muss fachlich korrekt, technisch reproduzierbar und organisatorisch verantwortbar sein. Bei manuellen E-Mail-Verfahren fehlen häufig Pflichtfelder, ein eindeutiger Genehmigungsstatus, eine standardisierte Zuordnung zu Rollen und ein zentraler Audit-Nachweis. Das Risiko besteht sowohl in zu weitreichenden als auch in nicht rechtzeitig entzogenen Berechtigungen.')
P('Zero Trust bedeutet in diesem Projekt nicht die vollständige Neugestaltung der Unternehmensarchitektur. Das Prinzip wird auf den ausgewählten Anwendungsfall übertragen: Jeder Antrag wird identitätsbezogen geprüft, jede Entscheidung wird explizit genehmigt, jede Berechtigung wird minimal vergeben und jeder Schritt wird protokolliert.')
H2('1.3 Projektziel')
P('Innerhalb von 70 aktiven Arbeitsstunden wird ein technisch funktionsfähiger Pilot entwickelt, der Rollenanforderungen erfasst, Pflichtfelder und Policies prüft, eine Genehmigungsentscheidung abbildet, die vorgesehene GitHub-Teamzuordnung ausführt beziehungsweise simuliert und einen strukturierten Audit-Eintrag erzeugt.')
goals=[['Ziel','Messgröße','Abnahmekriterium'],['Rollenmodell','mindestens 6 Pilotrollen','Rollenmatrix dokumentiert'],['Workflow','Antrag - Prüfung - Genehmigung - Provisioning - Benachrichtigung','End-to-End-Test nachvollziehbar'],['Audit','100 % der Pilotaktionen protokolliert','Audit-Eintrag mit Zeit, Akteur, Aktion und Ergebnis'],['Tests','12 definierte Testfälle','automatisierter Testlauf ohne kritischen Fehler'],['Dokumentation','Architektur, Betrieb, Nutzung, Risiken','vollständige Übergabeunterlagen']]
tab(goals,'SMART-orientierte Projektziele',widths=[36*mm,61*mm,58*mm])
H2('1.4 Projektbegründung')
P('Der Pilot reduziert das Projektrisiko gegenüber einer sofortigen unternehmensweiten Einführung. Er schafft eine belastbare Entscheidungsgrundlage, demonstriert die technische Integrationsfähigkeit und macht organisatorische Anforderungen sichtbar. Gleichzeitig begrenzt er Kosten und verhindert, dass im Prüfungsprojekt ein vollständiges Enterprise-IAM versprochen wird, das innerhalb von 70 Stunden nicht seriös realisierbar wäre.')
H2('1.5 Projektabgrenzung')
scope=[['Im Projekt enthalten','Nicht im Projekt enthalten'],['Rollen- und Berechtigungskatalog für den Pilot','Ablösung von Active Directory oder zentralem IDP'],['Self-Service-Formular und Genehmigungsworkflow','unternehmensweiter Produktivrollout'],['GitHub-API-/Actions-Integration','Privileged Access Management'],['Audit-Protokollierung und Export','vollständige Identitätsrezertifizierung'],['Testkonzept und Übergabedokumentation','rechtliche Bestätigung einer Revisionssicherheit']]
tab(scope,'Projektumfang und Abgrenzung',widths=[78*mm,78*mm])
callout('Die klare Abgrenzung ist ein zentrales Qualitätsmerkmal: Der Pilot liefert einen Machbarkeitsnachweis und eine skalierbare Referenzarchitektur, jedoch keine vollständige Identity-Governance-Plattform.')
H2('1.6 Rahmenbedingungen')
P('Die technische Umsetzung verwendet vorhandene beziehungsweise frei verfügbare Entwicklungswerkzeuge. Personenbezogene Produktivdaten werden nicht benötigt. Für Screenshots und Tests sind synthetische oder pseudonymisierte Testidentitäten einzusetzen. Externe Schnittstellen werden im Pilot nur mit minimalen Berechtigungen und getrennten Testzugängen angesprochen.')
fig(ARTIFACTS[0],'SWOT-Analyse des abgegrenzten Pilotprojekts')
H2('1.7 Projektauftrag')
P('Der Projektauftrag lautet: Planung, prototypische Umsetzung und Bewertung eines standardisierten Zero-Trust-Rollenworkflows mit GitHub-Integration. Der Auftrag umfasst die Projektsteuerung, Anforderungsanalyse, Variantenentscheidung, Architektur, Implementierung, Testdurchführung und Dokumentation. Die betriebliche Produktivfreigabe bleibt eine nachgelagerte Entscheidung des Auftraggebers.')
H2('1.8 Persönliche Projektrolle und Eigenleistung')
P('Ich übernahm die Rolle des Projektleiters und setzte zugleich die zentralen technischen Arbeitspakete des Piloten um. Zu meiner Eigenleistung gehörten die Strukturierung des Projektauftrags, die Erstellung der Ziel- und Anforderungsmatrix, die Auswahl und Bewertung der Lösungsvarianten, die Entwicklung der Zielarchitektur, die Umsetzung des Rollenworkflows, die Definition und Auswertung der Tests sowie das Projektcontrolling und die Abschlussdokumentation.')
P('Beratende Beiträge aus Datenschutz, Administration oder fachlicher Freigabe werden getrennt ausgewiesen. Die Verantwortung für organisatorische Freigaben verbleibt beim jeweiligen Auftraggeber beziehungsweise Rollenowner; technische Automatisierung ersetzt keine Managemententscheidung.')
story.append(PageBreak())

H1('2 Projektmanagement')
H2('2.1 Projektdefinition und Kick-off')
P('Zum Projektstart wurden Projektziel, Nicht-Ziele, Rollen, Kommunikationswege und die geplanten Liefergegenstände in einem Kick-off strukturiert. Die Detailplanung war noch nicht vollständig abgeschlossen; die abgestimmten Rahmenbedingungen reichten jedoch aus, um ein gemeinsames Projektverständnis herzustellen und Verantwortlichkeiten zu klären.')
kick=[['Agenda','Ergebnis'],['Ausgangslage und Nutzen','gemeinsames Verständnis des Sicherheits- und Automatisierungsbedarfs'],['Projektziel und Abgrenzung','70-Stunden-Pilot statt vollständigem Enterprise-IAM'],['Rollen und Verantwortungen','Projektleiter, Auftraggeber, IT-Administration, Datenschutz und Pilotnutzer abgegrenzt'],['Vorgehen und Meilensteine','hybrides Phasenmodell und sechs Freigabepunkte vereinbart'],['Kommunikation und Ablage','Statusbericht, Review-Protokoll und Repository als Projektakte festgelegt']]
tab(kick,'Kick-off-Ergebnisse',widths=[54*mm,102*mm],font=8.4)
P('Ein kompaktes Gesprächsprotokoll und ein Projektstatusbericht sind im Anhang als prüfbare Projektartefakte aufgenommen. Dadurch wird nicht nur beschrieben, dass Kommunikation stattgefunden hat, sondern auch, welche Entscheidungen und Verantwortlichkeiten daraus entstanden.')
H2('2.2 Vorgehensmodell')
P('Für den Pilot wird ein hybrides Vorgehensmodell eingesetzt. Projektauftrag, Zieldefinition, Architektur und Abnahmebedingungen werden planorientiert festgelegt. Die Umsetzung erfolgt iterativ in kurzen Entwicklungszyklen. Dadurch bleiben Scope, Termine und Prüfbarkeit stabil, während technische Erkenntnisse unmittelbar berücksichtigt werden können.')
P('Die iterative Umsetzung umfasst jeweils Planung, Implementierung, automatisierten Test und Review. Änderungen am Projektumfang werden nicht informell aufgenommen, sondern gegen Zeitbudget, Risiko und Nutzen bewertet.')
H2('2.3 Projektstrukturplan')
fig(ARTIFACTS[1],'Projektstrukturplan des Zero-Trust-Piloten')
H2('2.4 Zeit- und Aufwandplanung')
time_data=[['Phase laut Antrag','Wesentliche Arbeitspakete','Stunden'],['1 Projektinitialisierung und Analyse','Projektauftrag, Ist-Analyse, Anforderungen, Risikoprofil','15'],['2 Konzept und Architekturdesign','Zero-Trust-Framework, Architektur-Blueprint, Stakeholderfreigabe','15'],['3 Implementierung und GitHub-Integration','RBAC, Workflows, Schnittstellen, Audit- und Sicherheitsprüfungen','25'],['4 Test und Schulung','Funktionstests, Audit-Prüfung, Schulungskonzept und Feedback','8'],['5 Projektabschluss und Übergabe','Dokumentation, Abnahmevorbereitung, Lessons Learned und Übergabe','7'],['Gesamt','','70']]
tab(time_data,'Konsolidierte 70-Stunden-Planung',widths=[41*mm,97*mm,18*mm])
fig(ARTIFACTS[2],'Zeitlicher Projektverlauf im 13-Wochen-Rahmen laut Projektvorschlag')
H2('2.5 Ressourcenplanung')
res=[['Rolle / Ressource','Planwert','Verantwortung'],['Projektleiter Daniel Massa','70 aktive Prüfungsstunden','Projektauftrag, Analyse, Konzeption, Steuerung, Nachweise und Dokumentation'],['2 IT-Spezialisten','gemäß Projektvorschlag','Infrastruktur, technische Machbarkeit und Integration'],['1 Entwickler für Automatisierung','gemäß Projektvorschlag','GitHub-Workflows, Provisionierung und Schnittstellen'],['1 externer Compliance-Berater','gemäß Projektvorschlag','Compliance- und Sicherheitsreview'],['Projektcoach Carsten Vordermeier','projektbegleitend','fachliche Begleitung im Projekt-/Praktikumsbetrieb']]
tab(res,'Ressourcen und Verantwortlichkeiten',widths=[43*mm,32*mm,81*mm])
H2('2.6 Kostenplanung')
costs=[['Kosten-/Budgetbezug','Grundlage','Wert'],['Gesamtbudget','Projektvorschlag - Entwurfsdatum vor Abgabe zu bestätigen','ca. 50.000 EUR laut Entwurfsunterlagen'],['Budgetkategorien','Lizenzen, Schulung, externe Beratung','gemäß Projektvorschlag'],['Prüfungsaufwand Daniel Massa','aktive persönliche Projektarbeit','70 Stunden'],['Ist-Kosten','Angebote, Rechnungen und interne Verrechnungssätze','vor Abgabe nachzuweisen']]
tab(costs,'Einheitliche Kostenplanung',widths=[57*mm,57*mm,42*mm])
P('Die Kostenrechnung verwendet einen einheitlichen kalkulatorischen Stundensatz. Bereits vorhandene Plattformen und Open-Source-Komponenten werden nicht als neue Lizenzkosten angesetzt. Etwaige spätere Betriebs-, Support- oder Enterprise-Lizenzkosten sind nicht Bestandteil des Piloten und müssen vor einem Rollout separat bewertet werden.')
H2('2.7 Stakeholder- und Kommunikationsplanung')
fig(ARTIFACTS[3],'Stakeholder-Matrix')
comm=[['Stakeholder','Information','Taktung','Medium'],['Auftraggeber','Status, Entscheidungen, Risiken','Meilensteinbezogen','Review / Protokoll'],['IT-Administration','Architektur und Schnittstellen','wöchentlich','Technik-Review'],['Datenschutz','Datenfelder, Aufbewahrung, TOM','Konzept- und Testphase','Checkliste / Review'],['Pilotnutzer','Bedienung und Rückmeldung','Testphase','Kurzschulung / Feedback'],['Prüfungsdokumentation','Nachweise und Abweichungen','laufend','Repository / Projektakte']]
tab(comm,'Kommunikationsplan',widths=[37*mm,58*mm,31*mm,30*mm])
H2('2.8 Risiko- und Qualitätsplanung')
fig(ARTIFACTS[4],'Risikomatrix des Piloten')
riskdata=[['Risiko','Bewertung','Prävention','Reaktion'],['Fehlberechtigung','hoch','Rollenmatrix, Vier-Augen-Prinzip','Entzug, Audit, Ursachenanalyse'],['Secret-Leakage','hoch','Secrets Store, Scanner, Testtoken','Token sperren und ersetzen'],['Scope Creep','mittel','Abgrenzung, Change-Entscheidung','Anforderung verschieben'],['Zeitverzug','mittel','Meilensteine, Puffer, Priorisierung','Kann-Anforderung entfernen'],['Audit-Lücke','hoch','Pflichtlogging, Tests','Blockierung des Provisionings']]
tab(riskdata,'Risikobehandlung',widths=[37*mm,24*mm,49*mm,46*mm],font=8.2)
P('Qualitätskriterien sind Nachvollziehbarkeit, reproduzierbare Tests, eindeutige Anforderungen, minimale Berechtigungen, sichere Geheimnisverwaltung und konsistente Dokumentation. Eine Funktion gilt erst als abgeschlossen, wenn ihr Anforderungsbezug und ihr Testnachweis dokumentiert sind.')

H2('2.9 Meilensteine und Projektcontrolling')
P('Das Projektcontrolling verbindet Termin-, Kosten-, Qualitäts- und Umfangssteuerung. Zu jedem Meilenstein werden der erreichte Liefergegenstand, offene Risiken, verbrauchte Stunden und notwendige Entscheidungen dokumentiert. Reine Aktivitätsmeldungen reichen nicht aus; entscheidend ist der nachweisbare Fertigstellungsgrad.')
ms=[['Meilenstein','Liefergegenstand','Freigabekriterium'],['M1 Initiierung','Projektauftrag und Abgrenzung','Ziele, Scope und 70-h-Rahmen bestätigt'],['M2 Analyse','Anforderungen und Risikoregister','Muss-Anforderungen testbar formuliert'],['M3 Entwurf','Architektur und Datenmodell','Schnittstellen und Pilotgrenze geprüft'],['M4 Prototyp','lauffähiger End-to-End-Pfad','Dry-Run oder Test-API erfolgreich'],['M5 Test','Testprotokoll und Fehlerliste','keine offenen kritischen Befunde'],['M6 Abschluss','Dokumentation und Übergabepaket','Restmaßnahmen und Abnahmestatus eindeutig']]
tab(ms,'Meilenstein- und Freigabeplan',widths=[35*mm,62*mm,59*mm],font=8.2)
P('Bei einer erkennbaren Terminabweichung wird zuerst der Umfang der Kann-Anforderungen reduziert. Eine Erhöhung der offiziellen Prüfungszeit ist keine zulässige Standardreaktion. Technische Laufzeiten automatisierter Jobs werden nur dann als Arbeitszeit erfasst, wenn eine aktive Bearbeitung oder Auswertung stattfindet.')
story.append(PageBreak())
H2('2.10 RACI und Entscheidungswege')
P('Die RACI-Zuordnung verhindert Mehrfachverantwortung und ungeklärte Freigaben. Für jede kritische Aktivität wird genau eine accountable Rolle festgelegt. Das technische System kann Aktivitäten ausführen, aber keine organisatorische Verantwortung übernehmen.')
raci=[['Aktivität','Prüfling/PL','Auftraggeber','IT-Admin','Datenschutz','Pilotnutzer'],['Projektauftrag','R','A','C','C','I'],['Architektur','R','C','A/C','C','I'],['Rollenfreigabe','C','A','R','C','I'],['Implementierung','R/A','I','C','I','I'],['Datenschutzreview','C','I','C','R/A','I'],['Pilotabnahme','R','A','C','C','C']]
tab(raci,'RACI-Matrix',widths=[42*mm,27*mm,27*mm,24*mm,23*mm,22*mm],font=7.3)
P('Strategische Änderungen an Scope, Sicherheitsniveau oder betrieblicher Nutzung müssen durch den Auftraggeber entschieden werden. Der Projektleiter steuert die Umsetzung und dokumentiert Auswirkungen auf Zeit, Kosten, Risiko und Qualität.')
story.append(PageBreak())
H2('2.11 Change- und Claim-Management')
P('Änderungswünsche werden in einem Change-Log erfasst. Jeder Eintrag enthält Anlass, Nutzen, Aufwand, Risiko, Entscheidung und Zielversion. Im Prüfungsprojekt werden Änderungen nur umgesetzt, wenn sie ein Muss-Kriterium sichern oder ohne Gefährdung des Stundenrahmens realisierbar sind.')
changes=[['Change','Bewertung','Entscheidung'],['Produktives Azure-AD-SSO','hoher Integrations- und Freigabeaufwand','in Folgerollout verschoben'],['KI-Anomalieerkennung','kein Beitrag zu Muss-Kriterien','aus Scope entfernt'],['Hash-Verkettung im Audit','erhöht Manipulationserkennung','im Pilot umgesetzt'],['E-Mail-Eskalation','zusätzliche Abhängigkeit','als Mock/Benachrichtigung abgebildet']]
tab(changes,'Beispielhafte Änderungsentscheidungen',widths=[50*mm,60*mm,46*mm],font=8.1)
P('Claim-Management ist im internen Pilot nur eingeschränkt relevant. Dennoch werden Zusagen, Annahmen und Abhängigkeiten dokumentiert, damit aus einer informellen Erwartung keine unbemerkte Leistungsverpflichtung entsteht.')
story.append(PageBreak())
H2('2.12 Projektmarketing und Akzeptanz')
P('Projektmarketing richtet sich nicht auf werbliche Überhöhung, sondern auf Verständlichkeit und Akzeptanz. Die Kernbotschaft lautet: weniger unstrukturierte Rückfragen, nachvollziehbare Entscheidungen und klar definierte Rollen. Sicherheitskontrollen werden als Unterstützung eines verlässlichen Arbeitsprozesses erklärt.')
bullets(['Stakeholder erhalten zielgruppengerechte Informationen statt technischer Detailflut.','Pilotnutzer sehen Rollenbeschreibung, Bearbeitungsstatus und erwartete Genehmigungszeit.','Führungskräfte erhalten Risiko-, Nutzen- und Entscheidungsinformationen.','IT und Datenschutz erhalten technische Nachweise, Restmaßnahmen und Betriebsgrenzen.'])
P('Akzeptanz wird nicht nur über Zufriedenheitswerte bewertet. Ebenso relevant sind vollständige Anträge, geringe Rückfragen, korrekt ausgeführte Rollenentscheidungen und die Fähigkeit der Beteiligten, den Prozess ohne Projektteam zu bedienen.')
story.append(PageBreak())

H1('3 Spezifikationsphase und Lösungsentscheidung')
H2('3.1 Ist-Prozess')
P('Der betrachtete Ausgangsprozess ist durch unstrukturierte Anträge, manuelle Rückfragen und heterogene Nachweise geprägt. Typische Schritte sind Antrag, fachliche Zustimmung, technische Umsetzung und informelle Rückmeldung. Die Bearbeitungszeit hängt stark von Vollständigkeit und Verfügbarkeit der Beteiligten ab.')
P('Für die Projektplanung wird der Ist-Prozess qualitativ bewertet. Mengen- und Zeitwerte werden nur als Referenzszenario genutzt, solange keine belastbare Stichprobe mit Zeitraum, Fallzahl und Erhebungsmethode vorliegt. Diese Trennung verhindert, dass Planannahmen als gemessene Unternehmensleistung dargestellt werden.')
H2('3.2 Anforderungen')
req=[['ID','Anforderung','Typ','Priorität','Nachweis'],['A01','Rollenbasierte Berechtigungen','funktional','Muss','Rollenmatrix / TF07'],['A02','Strukturierter Self-Service-Antrag','funktional','Muss','Formular / TF01-TF02'],['A03','Explizite Genehmigungsentscheidung','funktional','Muss','Workflow / TF03-TF04'],['A04','GitHub-Teamzuordnung','funktional','Muss','API-/Simulationslog / TF07'],['A05','Audit-Protokollierung','nicht-funktional','Muss','Audit-Export / TF09-TF11'],['A06','Sicherer Rechteentzug','funktional','Muss','TF08'],['A07','Secret-Scanning','Sicherheit','Muss','TF10'],['A08','Betriebs- und Nutzerdokumentation','Organisation','Muss','Dokumentenpaket']]
tab(req,'Anforderungsmatrix',widths=[13*mm,60*mm,29*mm,20*mm,34*mm],font=7.8)
H2('3.3 Zero-Trust-Leitprinzipien')
bullets(['Explizite Verifikation jeder Rollenanforderung und Genehmigung.','Least Privilege: Rollen enthalten nur erforderliche Berechtigungen.','Assume Breach: Aktionen werden protokolliert und auf Fehlerpfade getestet.','Kurze Gültigkeit und definierter Entzug für zeitlich begrenzte Rollen.','Trennung von Antragsteller, Genehmiger und technischem Provisioning.'])
P('Die Prinzipien werden auf den Pilotprozess abgebildet. Netzwerksegmentierung, Device Posture, Continuous Access Evaluation oder vollständige Mikrosegmentierung sind nicht Bestandteil des Projekts.')
H2('3.4 Variantenvergleich und Make-or-Buy')
P('Bewertet werden der bestehende manuelle Prozess, eine Standard-IAM-/IGA-Lösung und ein begrenzter GitHub-Pilot. Eine Standardlösung kann die Kernanforderungen grundsätzlich abdecken, ist für den 70-Stunden-Nachweis jedoch mit höherem Lizenz-, Integrations- und Einführungsaufwand verbunden. Der Pilot wird deshalb als Lern- und Entscheidungsplattform gewählt, nicht weil Standardprodukte funktional ungeeignet wären.')
fig(ARTIFACTS[5],'Nutzwertvergleich der Lösungsvarianten')
variant=[['Kriterium','Gewicht','Manuell','Standard-IAM','GitHub-Pilot'],['Einführungskosten','15 %','5','2','4'],['Sicherheit','20 %','2','5','4'],['Automatisierung','20 %','1','5','4'],['Auditierbarkeit','20 %','1','5','4'],['Integration','15 %','2','4','5'],['Umsetzungsaufwand','10 %','5','2','4'],['Gewichtetes Ergebnis','100 %','2,35','4,10','4,15']]
tab(variant,'Nutzwertanalyse',widths=[48*mm,22*mm,27*mm,31*mm,28*mm],font=8.2)
P('Die exakten Ergebnisse liegen mit 4,10 Punkten für Standard-IAM und 4,15 Punkten für den GitHub-Pilot nur 0,05 Punkte auseinander. Die Auswahl des Piloten folgt deshalb nicht aus einer behaupteten funktionalen Überlegenheit, sondern aus dem engeren Lern-, Nachweis- und Umsetzungsumfang innerhalb des 70-Stunden-Rahmens.')
H2('3.5 Datenschutz- und Sicherheitsanforderungen')
P('Im Pilot werden nur Identifikatoren, Rollenbezug, Genehmigungsstatus, technische Ressource und Zeitstempel verarbeitet. Freitextbegründungen sind auf das notwendige Maß zu begrenzen. Produktive Personaldaten, besondere Kategorien personenbezogener Daten und private Inhalte sind ausgeschlossen.')
bullets(['Datenminimierung und Zweckbindung gemäß Art. 5 DSGVO.','Datenschutz durch Technikgestaltung gemäß Art. 25 DSGVO.','Angemessene technische und organisatorische Maßnahmen gemäß Art. 32 DSGVO.','Rollenbasierte Zugriffsrechte auf Audit- und Administrationsfunktionen.','Definiertes Lösch- und Aufbewahrungskonzept statt pauschaler unbegrenzter Speicherung.'])
callout('Eine Datenschutz-Folgenabschätzung ist nur dann als durchgeführt zu bezeichnen, wenn sie tatsächlich erstellt und durch die zuständige Stelle bewertet wurde. In dieser Fassung ist sie als Prüfpunkt, nicht als ungeprüfte Erfolgsaussage, enthalten.',risk=True)
H2('3.6 Budget- und Wirtschaftlichkeitsrahmen')
P('Der eingereichte Projektvorschlag nennt einen Budgetrahmen von ca. 50.000 EUR für Lizenzen, Schulung und externe Beratung. Dieser Betrag beschreibt den geplanten betrieblichen Projektumfang. Die 70 Prüfungsstunden des Prüfungsteilnehmers sind davon getrennt auszuweisen. Eine belastbare Wirtschaftlichkeitsrechnung erfordert zusätzlich reale Angebote, interne Verrechnungssätze, Betriebs- und Wartungskosten sowie gemessene Prozessmengen.')
fig(ARTIFACTS[11],'Budgetrahmen laut IHK-Projektvorschlag')
P('Da die vorliegenden Unterlagen keine freigegebene Detailkalkulation und keine belastbaren Ist-Prozessmengen enthalten, wird in dieser Fassung kein fiktiver Break-even behauptet. Die Nachkalkulation ist nach Projektabschluss aus Budget, Ist-Kosten, messbarer Zeitersparnis, Betriebskosten und Qualitätsnutzen zu erstellen.')

H2('3.7 Bedrohungsmodell')
P('Das Bedrohungsmodell betrachtet Missbrauchsfälle entlang des gesamten Rollenprozesses. Angreifer können versuchen, fremde Identitäten zu verwenden, Genehmigungen zu umgehen, Workflowdateien zu verändern, Tokens auszulesen oder Auditdaten zu manipulieren. Für jeden Bedrohungspfad wird eine präventive und eine detektive Kontrolle definiert.')
threat=[['Bedrohung','Angriffsweg','Kontrolle'],['Identitätsmissbrauch','gestohlene Sitzung oder Testidentität','MFA/SSO im Produktivbetrieb, kurze Sitzungen'],['Genehmigungsumgehung','direkter API-Aufruf','serverseitige Autorisierung und Statusmaschine'],['Workflow-Manipulation','ungeprüfter Commit','Branch Protection und Reviewpflicht'],['Token-Diebstahl','Secret im Code oder Log','Secrets Store, Scanner, Maskierung'],['Audit-Manipulation','direkter Datenbankzugriff','DB-Rollen, Append-only, Hash-Prüfung'],['Überberechtigung','zu breite Rollenmatrix','Least Privilege und Rollenowner']]
tab(threat,'Bedrohungen und Kontrollen',widths=[38*mm,53*mm,65*mm],font=8.0)
P('Das Modell dient der Priorisierung. Es ersetzt keinen Penetrationstest und keine formale Risikoanalyse für einen Produktivbetrieb.')
H2('3.8 Datenschutzbewertung der Datenfelder')
P('Die Datenschutzbewertung beginnt auf Feldebene. Für jedes Attribut werden Zweck, Rechtsgrundlage beziehungsweise betriebliche Erforderlichkeit, Zugriff, Aufbewahrung und Löschung beschrieben. Freitextfelder erhalten besondere Aufmerksamkeit, weil dort leicht unnötige personenbezogene Inhalte erfasst werden.')
datafields=[['Feld','Zweck','Aufbewahrung im Pilot','Schutz'],['user_id','Zuordnung des Antrags','bis Abschluss und definierte Nachweisfrist','pseudonymisierte Test-ID'],['role_id','beantragte Rolle','wie Vorgang','Rollen-Whitelist'],['reason','fachliche Begründung','kurz und ohne sensible Inhalte','Längen- und Inhaltshinweis'],['approver_id','Genehmigungsnachweis','wie Vorgang','rollenbasierter Zugriff'],['audit_hash','Integritätsprüfung','wie Auditdatensatz','nicht geheim, aber schreibgeschützt']]
tab(datafields,'Bewertung zentraler Datenfelder',widths=[31*mm,54*mm,39*mm,32*mm],font=7.9)
P('Eine feste Aufbewahrungsdauer wird nicht pauschal aus der DSGVO abgeleitet. Sie muss aus betrieblichen, rechtlichen und sicherheitsbezogenen Anforderungen begründet und durch eine zuständige Stelle freigegeben werden.')
story.append(PageBreak())
H2('3.9 Abnahmekriterien und Definition of Done')
P('Die Definition of Done verbindet fachliche Fertigstellung, technische Qualität und Dokumentation. Eine Funktion ist nicht abgeschlossen, wenn nur eine Benutzeroberfläche oder ein positiver Demonstrationspfad existiert.')
dod=[['Kriterium','Erforderlicher Nachweis'],['Anforderung eindeutig','ID, Priorität und Akzeptanzkriterium vorhanden'],['Implementierung geprüft','Review oder dokumentierter Selbstcheck'],['Positiv- und Negativtest','erwarteter Erfolg und erwartete Blockierung'],['Audit vollständig','Aktion, Akteur, Zeit, Ergebnis und Vorgangsbezug'],['Dokumentation aktualisiert','Nutzer-, Betriebs- und Architekturhinweis'],['Restfehler bewertet','Schweregrad, Workaround und Verantwortlicher']]
tab(dod,'Definition of Done',widths=[58*mm,98*mm],font=8.4)
P('Die Abnahmekriterien werden vor der Umsetzung festgelegt. Damit wird verhindert, dass nachträglich nur die erfolgreich demonstrierten Funktionen als Ziel ausgegeben werden.')
story.append(PageBreak())
H2('3.10 Nachkalkulation und Wirtschaftlichkeitsnachweis')
P('Die Nachkalkulation trennt verbindlich zwischen Budgetrahmen, Planwerten, tatsächlich angefallenen Kosten und messbarem Nutzen. Solange Angebote, Rechnungen, interne Verrechnungssätze und Pilotmessungen nicht vollständig vorliegen, werden weder Amortisationsdauer noch ROI als Projektergebnis behauptet.')
sens=[['Nachkalkulationsgröße','Quelle','Status'],['Budgetrahmen','IHK-Projektvorschlag','ca. 50.000 EUR'],['Lizenzkosten','Angebote / Rechnungen','vor Abgabe ergänzen'],['Schulungskosten','Angebote / Rechnungen','vor Abgabe ergänzen'],['externe Beratung','Vertrag / Rechnung','vor Abgabe ergänzen'],['interne Personalkosten','Verrechnungssätze / Zeiterfassung','vor Abgabe ergänzen'],['messbarer Nutzen','Pilotmessung und Prozessdaten','nach Pilot auswerten']]
tab(sens,'Sensitivitätsanalyse',widths=[35*mm,31*mm,38*mm,31*mm,31*mm],font=8.1)
P('Für eine Produktiventscheidung sind neben den einmaligen Kosten auch laufende Betriebs-, Support-, Lizenz- und Schulungskosten sowie qualitative Nutzenbeiträge zu berücksichtigen.')
story.append(PageBreak())

H1('4 Technische Konzeption')
H2('4.1 Zielarchitektur')
fig(ARTIFACTS[6],'Zielarchitektur und Pilotgrenze')
P('Die Zielarchitektur ist modular aufgebaut. Das React-Frontend erfasst Rollenanforderungen und zeigt Statusinformationen. FastAPI stellt REST-Endpunkte für Antrag, Genehmigung, Rollenprüfung und Export bereit. PostgreSQL speichert Rollen, Zuordnungen und Auditdaten. GitHub Actions beziehungsweise die GitHub API übernehmen die kontrollierte Automatisierung.')
P('Der zentrale Identity Provider bleibt außerhalb des Projekts. Für den Pilot kann die Authentisierung durch einen Testprovider oder signierte Testidentitäten simuliert werden. Eine produktive SSO-Integration erfordert ein separates Sicherheitsreview und eine abgestimmte Mandantenkonfiguration.')
H2('4.2 GitHub-Rollenworkflow')
fig(ARTIFACTS[7],'GitHub-basierter Rollenworkflow')
P('Der Workflow trennt fachliche und technische Verantwortlichkeiten. Ein Antrag wird zunächst syntaktisch validiert, anschließend gegen Policies geprüft und danach einem Genehmiger zugewiesen. Erst eine positive Entscheidung löst das Provisioning aus. Ablehnungen und technische Fehler führen zu keiner Rechtevergabe.')
H2('4.3 Rollen- und Berechtigungsmodell')
roles=[['Rolle','Zweck','Pilotberechtigungen'],['Admin','Administration des Piloten','Rollen und Policies verwalten, kein uneingeschränkter Produktivzugriff'],['Developer','Entwicklung in definierten Repositories','lesen/schreiben, Pull Requests'],['Reviewer','Qualitätssicherung','lesen, kommentieren, Review freigeben'],['Auditor','Nachweis und Prüfung','Audit-Logs und Exporte lesen'],['Read-Only','Informationszugriff','ausgewählte Repositories lesen'],['Approver','fachliche Genehmigung','Anträge genehmigen oder ablehnen']]
tab(roles,'Pilotrollen und Berechtigungsumfang',widths=[29*mm,50*mm,77*mm],font=8.2)
P('Das Rollenmodell vermeidet direkte Einzelberechtigungen, soweit dies technisch möglich ist. Rollen werden auf GitHub-Teams abgebildet. Jede Rolle erhält einen eindeutigen fachlichen Zweck, einen Genehmiger, zulässige Ressourcen und optional ein Ablaufdatum.')
H2('4.4 Datenmodell')
fig(ARTIFACTS[8],'RBAC-Datenmodell des Piloten')
P('Die Entitäten User, Role, Permission, Approval, GitHubTeam und AuditLog bilden die zentrale Nachweiskette. Viele-zu-viele-Beziehungen werden über Zuordnungstabellen realisiert. Audit-Einträge referenzieren den fachlichen Vorgang und enthalten keine unnötigen Inhaltsdaten.')
story.append(PageBreak())
H2('4.5 Audit- und Integritätskonzept')
fig(ARTIFACTS[9],'Hash-Verkettung der Audit-Ereignisse')
P('Auditdaten werden append-only geschrieben und über einen Hash des aktuellen sowie des vorherigen Eintrags verkettet. Damit werden nachträgliche Veränderungen erkennbar. Datenbankadministratoren oder Plattformbetreiber besitzen technisch weiterhin weitreichende Möglichkeiten; deshalb wird bewusst von Manipulationserkennung und nicht pauschal von rechtlich bestätigter Revisionssicherheit gesprochen.')
H2('4.6 Schnittstellen')
api=[['Schnittstelle','Methode/Protokoll','Zweck','Schutz'],['Portal - Backend','REST/HTTPS','Antrag und Status','Authentisierung, Validierung'],['Backend - GitHub','REST/HTTPS','Teamzuordnung','minimaler Token, Secrets Store'],['Backend - PostgreSQL','SQL/TLS','Rollen und Audit','DB-Rollen, Netzwerkgrenze'],['Workflow - Benachrichtigung','E-Mail/Mock','Statusmeldung','keine sensitiven Details'],['Audit - Export','CSV/JSON','Prüfnachweis','Auditor-Rolle, Filter']]
tab(api,'Schnittstellenübersicht',widths=[41*mm,36*mm,42*mm,37*mm],font=8.0)
H2('4.7 Technische Sicherheitsmaßnahmen')
bullets(['Keine Secrets im Repository; Nutzung eines Secrets Stores und kurzlebiger Testtoken.','Branch Protection, Reviewpflicht und automatisierte Prüfungen für sicherheitsrelevante Änderungen.','Eingabevalidierung, sichere Fehlerbehandlung und serverseitige Autorisierung.','Getrennte Test- und Produktivkonfigurationen.','Dependency- und Container-Scanning sowie dokumentierte Reaktion auf Findings.'])

H2('4.8 API-Vertrag und Statusmodell')
P('Die API bildet den Rollenprozess als explizite Zustandsmaschine ab. Zulässige Zustände sind DRAFT, SUBMITTED, VALIDATED, APPROVED, REJECTED, PROVISIONED, FAILED und REVOKED. Direkte Sprünge, beispielsweise von SUBMITTED zu PROVISIONED, werden serverseitig verhindert.')
api2=[['Methode','Pfad','Zulässige Rolle','Ergebnis'],['POST','/role-requests','Antragsteller','Antrag in SUBMITTED'],['POST','/role-requests/{id}/validate','System','VALIDATED oder REJECTED'],['POST','/role-requests/{id}/approve','Genehmiger','APPROVED'],['POST','/role-requests/{id}/provision','Provisioner/System','PROVISIONED oder FAILED'],['POST','/role-requests/{id}/revoke','Administrator','REVOKED'],['GET','/audit/export','Auditor','gefilterter Nachweisexport']]
tab(api2,'API- und Berechtigungsvertrag',widths=[24*mm,58*mm,37*mm,37*mm],font=7.8)
P('Idempotency-Keys verhindern doppelte Ausführung bei Wiederholungen. Fehlerantworten enthalten eine Korrelations-ID, aber keine Tokens, Stacktraces oder vertraulichen Konfigurationswerte.')
story.append(PageBreak())
H2('4.9 Deployment- und Konfigurationskonzept')
P('Die Pilotumgebung besteht aus getrennten Containern für Frontend, Backend und Datenbank. Konfigurationen werden über Umgebungsvariablen beziehungsweise Secrets eingebunden. Ein Compose-Setup unterstützt die lokale Reproduzierbarkeit; ein späteres produktives Deployment ist davon getrennt zu planen.')
deploy=[['Komponente','Pilotbetrieb','Produktivanforderung'],['Frontend','lokaler Container oder statischer Testhost','TLS, CSP, Monitoring'],['Backend','FastAPI-Container','Reverse Proxy, Rate Limits, Hochverfügbarkeit'],['PostgreSQL','isolierte Testdatenbank','Backup, Restore-Test, DB-Rollen'],['GitHub-Zugang','Testorganisation oder Dry-Run','App-Installation mit minimalen Scopes'],['Secrets','lokale sichere Variable / CI Secret','zentraler Vault und Rotation']]
tab(deploy,'Deployment-Grenzen',widths=[43*mm,52*mm,61*mm],font=8.1)
P('Die Pilotkonfiguration ist nicht unverändert in Produktion zu übernehmen. Insbesondere Authentisierung, Schlüsselverwaltung, Backup, Monitoring und Netzwerksegmentierung benötigen eine separate Freigabe.')
story.append(PageBreak())
H2('4.10 Fehler-, Retry- und Wiederanlaufkonzept')
P('Externe API-Aufrufe können trotz korrekter Fachlogik scheitern. Der Workflow unterscheidet fachliche Ablehnung, temporären technischen Fehler und permanenten technischen Fehler. Nur temporäre Fehler werden begrenzt wiederholt.')
retry=[['Fehlerklasse','Beispiel','Behandlung'],['fachlich','Policy verletzt','sofortige Ablehnung, keine Wiederholung'],['temporär','Timeout oder Rate Limit','maximal drei Retries mit Backoff'],['permanent','ungültiger Token-Scope','FAILED, Alarm und manuelle Klärung'],['unklarer Status','Antwort nach Timeout unbekannt','Ist-Zustand über API prüfen, nicht blind erneut provisionieren'],['Auditfehler','Log kann nicht geschrieben werden','Provisioning blockieren oder kompensieren']]
tab(retry,'Fehlerbehandlung',widths=[35*mm,50*mm,71*mm],font=8.0)
P('Ein erfolgreicher API-Status allein genügt nicht. Nach dem Provisioning wird der Zielzustand gelesen und mit dem erwarteten Team- beziehungsweise Rollenstatus verglichen.')
story.append(PageBreak())
H2('4.11 Logging, Monitoring und Datenschutz')
P('Betriebslogs und Auditlogs erfüllen unterschiedliche Zwecke. Betriebslogs unterstützen Fehleranalyse und Performancebeobachtung; Auditlogs dokumentieren fachlich relevante Sicherheitsereignisse. Beide Datenarten werden getrennt klassifiziert und mit unterschiedlichen Zugriffsrechten versehen.')
logtab=[['Logart','Inhalt','Zugriff','Ausschluss'],['Betriebslog','Korrelations-ID, Dauer, Fehlercode','Betrieb/Entwicklung','Tokens, Passwörter, vollständige Begründungen'],['Auditlog','Akteur, Aktion, Ressource, Ergebnis','Auditor/Compliance','technische Stacktraces'],['Security-Finding','Scanner, Schweregrad, Fundstelle','Security/Owner','unnötige personenbezogene Daten']]
tab(logtab,'Logging-Kategorien',widths=[33*mm,52*mm,36*mm,35*mm],font=7.8)
P('Monitoring-Kennzahlen umfassen Fehlerrate, Workflowdauer, Retry-Anzahl, abgelehnte Anträge und Audit-Schreibfehler. Schwellenwerte werden im Pilot beobachtet, aber erst nach ausreichender Datenbasis als SLA festgelegt.')
story.append(PageBreak())

H1('5 Durchführungsphase')
H2('5.1 Entwicklungsumgebung und Repository')
P('Die Umsetzung erfolgt in einem versionierten Repository mit klarer Verzeichnisstruktur für Backend, Frontend, Workflows, Tests und Dokumentation. Lokale Dienste werden über Container gestartet. Die CI-Pipeline führt Linting, Unit-Tests, Sicherheitsprüfungen und einen Build-Check aus.')
H2('5.2 Backend und Policy-Prüfung')
P('Das FastAPI-Backend stellt typisierte Endpunkte bereit. Pydantic-Modelle validieren Pflichtfelder und erlaubte Werte. Die Policy-Schicht prüft Rollen, Ressourcen, Genehmiger und Trennung kritischer Funktionen. Nicht zulässige Kombinationen werden vor dem Provisioning blockiert und protokolliert.')
H2('5.3 Self-Service-Oberfläche')
P('Die React-Oberfläche umfasst Dashboard, Rollenformular, Statusansicht und eine eingeschränkte Administrationsansicht. Rollenbeschreibungen und erwartete Genehmiger werden direkt im Formular angezeigt. Fehlermeldungen erläutern den nächsten Schritt, ohne technische oder sicherheitsrelevante Interna offenzulegen.')
H2('5.4 GitHub-Automatisierung')
P('Ein Workflow übernimmt Validierung, Genehmigungsabfrage, Provisioning und Benachrichtigung. Für den Pilot wird zwischen echter API-Ausführung und Dry-Run unterschieden. Der Dry-Run erzeugt denselben Auditpfad, verändert aber keine externe Teamzuordnung. Dadurch kann der Prozess sicher vorgeführt und getestet werden.')
H2('5.5 Audit-Protokollierung')
P('Jeder Zustandswechsel erzeugt ein strukturiertes Ereignis. Pflichtfelder sind Vorgangs-ID, Zeitstempel, Akteur beziehungsweise Systemkomponente, Aktion, Ergebnis und Referenz auf den vorherigen Hash. Exporte werden gefiltert und nur der Auditor-Rolle bereitgestellt.')
H2('5.6 Qualitätssicherung in der Umsetzung')
bullets(['Pull-Request-Review für sicherheitskritische Änderungen.','Unit-Tests für Validierung und Policies.','Integrationstests für Antrag, Genehmigung, Provisioning und Audit.','Secret- und Dependency-Scanning.','Traceability von Anforderung über Implementierung zum Testfall.'])
fig(ARTIFACTS[13],'Traceability von Anforderungen, Realisierung und Nachweis')
H2('5.7 Abweichungsmanagement')
P('Erkenntnisse, die den 70-Stunden-Rahmen überschreiten, werden als Restmaßnahme dokumentiert. Dazu gehören produktive SSO-Anbindung, organisationsweite Rollenkataloge, Rezertifizierung, Hochverfügbarkeit und SIEM-Integration. Diese Funktionen werden nicht verdeckt in den Pilot aufgenommen, sondern priorisiert in eine Roadmap überführt.')

H2('5.8 Implementierungsentscheidungen')
P('FastAPI wurde gewählt, weil typisierte Request-Modelle, automatische OpenAPI-Dokumentation und eine klare Trennung der Services den Pilot unterstützen. React ermöglicht eine übersichtliche Self-Service-Oberfläche. PostgreSQL stellt Transaktionen, Constraints und flexible Auswertungen für Rollen- und Auditdaten bereit.')
P('Die Technologieentscheidung ist kein allgemeines Urteil über andere Stacks. Entscheidend waren vorhandene Kenntnisse, Reproduzierbarkeit, Testbarkeit und der begrenzte Projektumfang. Ein Wechsel des Stacks hätte keinen ausreichenden zusätzlichen Projektnutzen erzeugt.')
impl=[['Entscheidung','Begründung','Konsequenz'],['FastAPI statt gemischter Backend-Stacks','einheitliche Python-Codebasis','weniger Toolwechsel und Widersprüche'],['Dry-Run für Provisioning','sicherer Demonstrationsbetrieb','Produktivwirkung separat freigeben'],['Hash-Verkettung','Manipulationen erkennbar machen','keine Behauptung formaler Revisionssicherheit'],['Rollen statt Einzelrechte','Wartbarkeit und Least Privilege','Rollenowner erforderlich']]
tab(impl,'Zentrale Implementierungsentscheidungen',widths=[44*mm,65*mm,47*mm],font=8.0)
story.append(PageBreak())
H2('5.9 Dokumentations- und Repository-Struktur')
P('Die Projektdokumentation und der technische Stand müssen auf denselben Liefergegenstand verweisen. Repository, Testbericht, Screenshots und PDF dürfen keine widersprüchlichen Technologien oder Statusangaben enthalten.')
repo=[['Pfad','Inhalt'],['src/backend/','FastAPI-Endpunkte, Policies und Audit-Service'],['src/frontend/','React-Komponenten und Formulare'],['.github/workflows/','CI, Tests und Rollenworkflow'],['tests/','Unit-, Integrations- und Sicherheitstests'],['docs/','Architektur, Betrieb, Nutzung und Entscheidungen'],['reports/','reproduzierbare Test- und Scanergebnisse']]
tab(repo,'Empfohlene Repository-Struktur',widths=[52*mm,104*mm],font=8.4)
P('Generierte Artefakte erhalten Version, Erstellzeitpunkt und Quellbezug. Screenshots werden als Simulation, Testumgebung oder Produktivansicht gekennzeichnet, damit ihre Aussagekraft eindeutig bleibt.')
story.append(PageBreak())

H1('6 Test- und Pilotphase')
H2('6.1 Teststrategie')
P('Die Teststrategie kombiniert Unit-, Integrations-, Sicherheits- und Abnahmetests. Testdaten sind synthetisch. Jeder Muss-Anforderung ist mindestens ein Testfall zugeordnet. Kritische Fehler in Autorisierung, Provisioning oder Audit blockieren die Freigabe.')
H2('6.2 Testfälle')
tests=[['ID','Testobjekt','Erwartetes Ergebnis','Ergebnis*','Commit / Version','Laufzeit'],['TF01','Rollenantrag','gültiger Antrag wird angelegt','bestanden','offen','offen'],['TF02','Pflichtfelder','unvollständiger Antrag wird abgewiesen','bestanden','offen','offen'],['TF03','Genehmigung','positive Entscheidung setzt Workflow fort','bestanden','offen','offen'],['TF04','Ablehnung','keine Rechtevergabe','bestanden','offen','offen'],['TF05','Policy erlaubt','zulässige Kombination wird akzeptiert','bestanden','offen','offen'],['TF06','Policy blockiert','unzulässige Kombination wird gestoppt','bestanden','offen','offen'],['TF07','Provisioning','Teamzuordnung oder Dry-Run erfolgreich','bestanden','offen','offen'],['TF08','Rechteentzug','Rolle wird entzogen und protokolliert','bestanden','offen','offen'],['TF09','Audit-Eintrag','vollständiges Ereignis vorhanden','bestanden','offen','offen'],['TF10','Secret-Scan','kein produktives Secret gefunden','bestanden','offen','offen'],['TF11','Audit-Export','gefilterter Export wird erzeugt','bestanden','offen','offen'],['TF12','Benachrichtigung','Statusmeldung wird erstellt','bestanden','offen','offen']]
tab(tests,'Testfallmatrix - Evidenzstatus',widths=[10*mm,29*mm,54*mm,19*mm,25*mm,19*mm],font=6.6)
fig(ARTIFACTS[10],'Ergebnisübersicht des in den Unterlagen ausgewiesenen Pilot-Testlaufs')
P('* Die Ergebnisangabe „bestanden“ stammt aus den vorliegenden Projektunterlagen. Commit oder Version und Laufzeit sind noch nicht durch einen zugeordneten Repository-Testreport belegt. Bis zur Zuordnung bleibt der reproduzierbare Nachweis offen.')
P('Der Teststatus beschreibt den technischen Pilotstand. Er ist kein Nachweis eines unternehmensweiten Produktivbetriebs. Für eine spätere Abnahme sind zusätzlich reale Rollenverantwortliche, produktive Schnittstellen, Datenschutzfreigabe und Betriebsanforderungen zu prüfen.')
H2('6.3 Fehler- und Abweichungsanalyse')
errors=[['Befund','Auswirkung','Korrektur'],['fehlender Zeitstempel in Audit-Event','Nachweis unvollständig','Pflichtfeld und Negativtest ergänzt'],['unklare Admin-Rollenabgrenzung','zu hohe Berechtigung möglich','Rolle getrennt und Policy verschärft'],['fehlende Ablehnungsbenachrichtigung','Status für Antragsteller unklar','Notification-Pfad ergänzt'],['API-Fehler ohne Retry','temporärer Ausfall führt zu Abbruch','begrenzter Retry und Fehlerstatus']]
tab(errors,'Behobene Pilotbefunde',widths=[48*mm,51*mm,57*mm],font=8.2)
H2('6.4 Soll-Ist-Vergleich')
si=[['Kriterium','Soll','Pilot-Ist','Bewertung'],['Rollenmodell','mindestens 6 Rollen','6 Rollen dokumentiert','erreicht'],['Workflow','5 Prozessstufen','5 Stufen mit Fehlerpfad','erreicht'],['Audit','vollständige Pilotereignisse','strukturierter Export und Hash-Kette','erreicht'],['Tests','12 definierte Testfälle','12/12 laut Projektunterlagen; Testreport beizulegen','nachzuweisen'],['Produktivbetrieb','nicht Bestandteil','nicht durchgeführt','abgegrenzt'],['Betriebliche Abnahme','separater Nachweis','vor Produktivfreigabe erforderlich','offen']]
tab(si,'Soll-Ist-Vergleich',widths=[39*mm,38*mm,52*mm,27*mm],font=8.2)
H2('6.5 Abnahmevoraussetzungen')
P('Eine endgültige betriebliche Abnahme darf erst dokumentiert werden, wenn eine berechtigte auftraggebende Stelle die Muss-Kriterien geprüft und ein Abnahmeprotokoll unterzeichnet hat. Die vorliegende Arbeit enthält deshalb eine Abnahmevorlage, aber keine erfundene Unterschrift oder unbestätigte Freigabe.')
callout('Vor IHK-Einreichung müssen tatsächliche Abnahme, Testprotokolle, Repository-Stand und Projektzeitnachweis miteinander übereinstimmen.',risk=True)

story.append(PageBreak())
H2('6.6 Evidenz- und Reproduzierbarkeitskonzept')
P('Ein Testergebnis ist nur dann belastbar, wenn Testversion, Eingabedaten, erwartetes Ergebnis und tatsächliches Ergebnis nachvollziehbar sind. Die Dokumentation verweist deshalb auf automatisierte Reports und nicht ausschließlich auf dekorative Screenshots.')
evidence=[['Nachweis','Mindestinhalt'],['Testreport','Commit/Version, Test-ID, Ergebnis, Laufzeit'],['Security-Scan','Scanner-Version, Scope, Findings und Bewertung'],['API-Nachweis','Request-Korrelation, Status und verifizierter Zielzustand'],['Audit-Export','Vorgangs-ID, vollständige Ereigniskette, Hash-Prüfung'],['Screenshot','Umgebung, Zeitpunkt, Simulation/Test/Produktion']]
tab(evidence,'Mindestanforderungen an Projektnachweise',widths=[48*mm,108*mm],font=8.3)
P('Persönliche Daten und Secrets werden vor der Aufnahme in die Projektarbeit anonymisiert. Eine visuelle Darstellung darf den Sachverhalt verdeutlichen, aber keine nicht vorhandene Produktivumgebung vortäuschen.')
story.append(PageBreak())
H2('6.7 Abnahme- und Restpunktelogik')
P('Die Abnahme unterscheidet kritische, wesentliche und geringfügige Restpunkte. Kritische Restpunkte verhindern jede Freigabe. Wesentliche Restpunkte erlauben höchstens eine eingeschränkte Pilotfreigabe mit Termin und Verantwortlichem. Geringfügige Punkte können dokumentiert nachgezogen werden.')
restlogic=[['Klasse','Beispiel','Freigabewirkung'],['kritisch','Autorisierung umgehbar, Audit fehlt, Secret exponiert','keine Freigabe'],['wesentlich','Retry/Benachrichtigung unvollständig','nur begrenzter Pilot mit Maßnahme'],['geringfügig','Text- oder Darstellungsfehler','Freigabe möglich, Nacharbeit terminieren']]
tab(restlogic,'Klassifizierung von Abnahmebefunden',widths=[33*mm,67*mm,56*mm],font=8.1)
P('Die Entscheidung wird im Abnahmeprotokoll festgehalten. Ein leeres Formular oder eine vom Projektverfasser selbst eingesetzte Unterschrift ist kein Abnahmenachweis.')
H2('6.8 Projektstatusbericht zum Dokumentationsstichtag')
status=[['Dimension','Status','Begründung / Maßnahme'],['Leistung','grün','Muss-Funktionen des technischen Piloten und Dokumentation vorhanden'],['Zeit','gelb','finale Ist-Zeiten sind mit dem persönlichen Zeitnachweis abzugleichen'],['Kosten','grün','kalkulatorische Kostenbasis konsistent; keine neuen Enterprise-Lizenzen'],['Qualität','gelb','Anforderungs-Test-Zuordnung dokumentiert; Commit-/Laufzeitnachweis noch offen'],['Betriebliche Abnahme','gelb','Unterzeichnung und betriebliche Freigabe bleiben gesonderter Auftraggebernachweis']]
tab(status,'Projektstatusbericht',widths=[32*mm,22*mm,102*mm],font=8.3)
P('Der Gesamtstatus wird nach der ungünstigsten Einzelbewertung als gelb geführt. Der technische Pilot ist abgeschlossen; für eine betriebliche Produktivfreigabe sind insbesondere die benannten Owner, der produktive Identity Provider, Datenschutzfreigaben und ein unterzeichnetes Abnahmeprotokoll erforderlich.')
story.append(PageBreak())

H1('7 Rollout, Schulung und Betriebsübergabe')
H2('7.1 Pilotbetrieb')
P('Der Pilotbetrieb erfolgt mit einem kleinen, kontrollierten Nutzerkreis und synthetischen beziehungsweise freigegebenen Testidentitäten. Zunächst werden nur unkritische Rollen und Test-Repositories einbezogen. Der Rollout wird gestoppt, wenn ein kritischer Fehler in Autorisierung, Audit oder Rechteentzug auftritt.')
H2('7.2 Schulungs- und Kommunikationskonzept')
bullets(['30-minütige Einweisung für Antragsteller und Genehmiger.','Administrator-Guide für Rollenpflege, Fehlerstatus und Audit-Export.','Kurzanleitung mit Rollenbeschreibung, Genehmigungsweg und Supportkontakt.','Feedbackkanal für Unklarheiten und Verbesserungswünsche.'])
H2('7.3 Betriebsübergabe')
P('Die Übergabe umfasst Architekturübersicht, Deployment-Anleitung, Rollenmatrix, Schnittstellenbeschreibung, Testprotokoll, Restmaßnahmen und Notfallhinweise. Ein Betrieb ohne benannten Owner, Backup-Verfahren und Secret-Rotation ist nicht zulässig.')
H2('7.4 Rollout- und Skalierungsroadmap')
fig(ARTIFACTS[12],'Einführungs- und Skalierungsroadmap')
P('Erst nach Stabilisierung des Piloten folgt eine mögliche Integration in einen zentralen Identity Provider oder eine IGA-Plattform. Die Pilotkomponenten können dabei als Referenz für Genehmigungslogik, Rollenbeschreibung und Audit-Nachweise weiterverwendet werden.')

H2('7.5 Betriebsmodell und Verantwortungsübergang')
P('Nach dem Pilot benötigt jede Komponente einen Owner. Fachliche Rollenowner entscheiden über Inhalt und Genehmigungsweg; der technische Owner verantwortet Verfügbarkeit, Secrets, Updates und Fehlerbehandlung; Datenschutz und Informationssicherheit prüfen die vorgesehenen Kontrollen.')
ops=[['Verantwortung','Aufgabe'],['Service Owner','Nutzen, Budget, Freigaben und Prioritäten'],['Rollenowner','Berechtigungsinhalt und Rezertifizierung'],['Technischer Betrieb','Deployment, Backup, Monitoring, Incident-Behandlung'],['Security/Datenschutz','Kontrollreview, Findings und Aufbewahrung'],['Support','Anwenderfragen und standardisierte Eskalation']]
tab(ops,'Betriebsrollen',widths=[46*mm,110*mm],font=8.4)
P('Die Übergabe ist erst vollständig, wenn Zugänge, Dokumentation, Notfallkontakte, bekannte Einschränkungen und Restmaßnahmen übergeben und verstanden wurden.')
story.append(PageBreak())

H1('8 Projektabschlussphase und Wirtschaftlichkeit')
H2('8.1 Projektergebnis')
P('Das Projekt liefert einen abgegrenzten und testbaren Zero-Trust-Rollenworkflow. Die zentrale Leistung besteht nicht in einer vollständigen IAM-Einführung, sondern in der strukturierten Übersetzung von fachlichen Anforderungen in Rollen, Policies, technische Schnittstellen und reproduzierbare Nachweise.')
H2('8.2 Kosten- und Nutzenbewertung')
P('Der Projektvorschlag nennt einen Budgetrahmen von ca. 50.000 EUR. Eine belastbare Nachkalkulation kann erst nach Einsetzen der tatsächlichen Lizenz-, Schulungs-, Beratungs- und internen Personalkosten sowie der gemessenen Prozessverbesserung erfolgen.')
H2('8.3 Lessons Learned')
bullets(['Eine enge Projektabgrenzung erhöht Glaubwürdigkeit und Prüfbarkeit.','Zeit- und Kostenmodelle müssen aus einer einzigen konsistenten Basis stammen.','Technische Screenshots ersetzen keine nachvollziehbare Anforderungs- und Testkette.','Auditierbarkeit ist präziser zu beschreiben als pauschale Revisionssicherheit.','Standard-IAM-Lösungen sind nicht funktional abzuwerten; die Entscheidung muss projektspezifisch erfolgen.','Produktivwerte, Pilotwerte, Planwerte und belegte Ist-Werte müssen sichtbar getrennt werden.'])
H2('8.4 Restrisiken')
rest=[['Restrisiko','Maßnahme vor Rollout'],['Betriebsverantwortung ungeklärt','Owner und Supportmodell benennen'],['Produktive SSO-Integration ungeprüft','Security- und Datenschutzreview durchführen'],['Rollen wachsen unkontrolliert','Owner, Ablaufdatum und Rezertifizierung definieren'],['Auditdaten werden zu lange gespeichert','Aufbewahrungs- und Löschkonzept freigeben'],['GitHub-/API-Abhängigkeit','Fehlerbetrieb, Limits und Exit-Option dokumentieren']]
tab(rest,'Restrisiken und Folgemaßnahmen',widths=[69*mm,87*mm])
H2('8.5 Persönliches Fazit')
P('Die Projektarbeit verbindet Projektmanagement, Wirtschaftlichkeit, Datenschutz und technische Umsetzung. Der wichtigste Erkenntnisgewinn liegt in der konsequenten Trennung zwischen einem realistisch umsetzbaren Pilot und einer späteren Unternehmenslösung. Durch die konsistente Nachweiskette kann der Pilot sachlich bewertet und gezielt weiterentwickelt werden.')

H2('8.6 Gesamtbewertung gegen das magische Dreieck')
P('Das Projekt wird abschließend gegen Leistung, Zeit und Kosten bewertet. Der Leistungsumfang wurde im Prüfungsnachweis auf einen Pilot begrenzt. Der persönliche aktive Prüfungsaufwand beträgt 70 Stunden; der betriebliche Budgetrahmen des Projektvorschlags beträgt ca. 50.000 EUR. Qualitäts- und Sicherheitskriterien werden nicht zugunsten zusätzlicher Funktionen abgesenkt.')
triangle=[['Dimension','Ergebnis','Bewertung'],['Leistung','Muss-Funktionen des Piloten und Dokumentation','erfüllt, Produktivumfang abgegrenzt'],['Zeit','70 aktive Prüfungsstunden im 13-Wochen-Rahmen','Planbasis gemäß Projektvorschlag'],['Kosten','ca. 50.000 EUR Budgetrahmen','Ist-Kosten nachzuweisen'],['Qualität','Traceability, Tests und Restpunktelogik','nachweisorientiert'],['Risiko','kritische Produktivthemen in Roadmap verschoben','kontrolliert']]
tab(triangle,'Abschlussbewertung',widths=[35*mm,66*mm,55*mm],font=8.1)
P('Die wichtigste Steuerungsentscheidung war der Verzicht auf eine überzogene Vollimplementierung. Dadurch bleibt das Ergebnis fachlich verteidigbar und lässt sich anhand konkreter Artefakte demonstrieren.')
story.append(PageBreak())

H1('9 Quellen und methodische Grundlagen')
H2('9.1 Quellenstatus')
refs=['IHK-Projektvorschlag Daniel Massa, Prüflingsnummer 615951, Zero-Trust-Sicherheitskonzept mit GitHub-Integration, Entwurfsfassung; Datum vor Abgabe zu bestätigen.',
'NIST: SP 800-207, Zero Trust Architecture, 2020.',
'ISO/IEC 27001:2022, Information security management systems - Requirements.',
'ISO/IEC 27002:2022, Information security controls.',
'Verordnung (EU) 2016/679, insbesondere Art. 5, 25 und 32.',
'BSI: IT-Grundschutz-Kompendium, Bausteine zu Identitäts- und Berechtigungsmanagement.',
'GitHub Documentation: GitHub Actions und REST API.',
'Projektmanagement-Unterlagen und IHK-Lehrgangsmaterialien des Nutzers, insbesondere Projektanbahnung, Projektorganisation und Technischer Entwurf.',
'Formale Richtlinie Projektarbeit IT Professional, bereitgestellte Fassung November 2021.',
'Projektdokumentation Certified IT Business Manager - Kommunikationsplattform, ausschließlich Struktur- und Formatreferenz; keine inhaltliche Quelle.',
'Projektarbeit HOMAG Partner Portal, ausschließlich Struktur- und Formatreferenz; keine inhaltliche Quelle.',
'Projektdokumentation StreamServe-Migration, ausschließlich Struktur- und Formatreferenz; keine inhaltliche Quelle.'
]
for i,r in enumerate(refs,1): P(f'{i}. {r}')
P('Die Web- und Herstellerdokumentation ist vor der Abgabe auf Version, Abrufdatum und konkrete Kapitelangabe zu prüfen. Interne Quellen sind mit Titel, Version, Datum und Freigabestatus zu benennen.')
H2('9.2 KI- und Werkzeugtransparenz')
P('Bei der Erstellung wurden KI-gestützte Werkzeuge zur sprachlichen Prüfung, Strukturkontrolle und visuellen Ideengenerierung eingesetzt. Das Deckblatt enthält ein KI-generiertes Gestaltungselement; die fachlichen Diagramme, Tabellen und Berechnungen wurden reproduzierbar im Python-/ReportLab-Build erzeugt. Sämtliche fachlichen Aussagen, Kennzahlen, Quellen und Nachweise müssen durch den Verfasser geprüft und verantwortet werden. Eine KI-Ausgabe gilt nicht als Projektnachweis.')
story.append(PageBreak())

P('Eidesstattliche Erklärung','FrontH')
P('Ich versichere, dass ich die vorliegende Projektarbeit selbstständig verfasst und keine anderen als die angegebenen Quellen und Hilfsmittel benutzt habe. Alle Stellen, die wörtlich oder sinngemäß aus veröffentlichten oder nicht veröffentlichten Quellen übernommen wurden, sind als solche kenntlich gemacht.')
Spacer(1,20)
P('Stuttgart, den 01.11.2026')
story.append(Spacer(1,25*mm))
P('__________________________________<br/>Daniel Massa')
story.append(PageBreak())

# Appendices
H1('Anhang')
H2('A1 Projektstammdaten und Zeitplan')
stammdaten=[['Feld','Bestätigter Wert'],['Prüfungsteilnehmer','Daniel Massa'],['Prüflingsnummer','615951'],['Wohnanschrift','Hackstraße 41, 70190 Stuttgart'],['Mobiltelefon','+49 178 2989360'],['E-Mail','Massa.Daniel@proton.me'],['Projekt-/Praktikumsbetrieb','Verein zur Förderung der Berufsbildung e. V.'],['Betriebsanschrift','Kurfürstenstraße 6, 71636 Ludwigsburg'],['Projektumfeld','IT-Projektmanagement / IT-Sicherheit / digitale Verwaltung / Zugriffskontrolle'],['Projektcoach','Carsten Vordermeier'],['Kontakt Projektcoach','07136 396663 / vordermeier@c-tim.de'],['Projektvorschlag','Entwurfsfassung; Datum vor Abgabe zu bestätigen'],['Abgabedatum Dokumentation','01.11.2026'],['Projektlaufzeit laut Vorschlag','13 Wochen'],['Budgetrahmen laut Vorschlag','ca. 50.000 EUR']]
tab(stammdaten,'Stammdaten aus der vorliegenden Entwurfsfassung',widths=[58*mm,98*mm],font=8.3)
H2('A1.1 Detaillierter Zeitplan')
tab(time_data,'Detaillierte Aufwandssicht',widths=[45*mm,86*mm,25*mm])
H2('A2 Projektstrukturplan')
fig(ARTIFACTS[1],'Projektstrukturplan - Anhangswiederholung',width=160*mm,maxh=160*mm)
story.append(PageBreak())
H2('A3 Risikoanalyse')
fig(ARTIFACTS[4],'Risikomatrix - Anhangswiederholung')
tab(riskdata,'Risikoregister',widths=[37*mm,24*mm,49*mm,46*mm],font=8.2)
story.append(PageBreak())
H2('A4 Architektur und Workflow')
fig(ARTIFACTS[6],'Zielarchitektur - Detailansicht')
fig(ARTIFACTS[7],'Workflow - Detailansicht')
story.append(PageBreak())
H2('A5 Datenmodell und Audit')
fig(ARTIFACTS[8],'Datenmodell - Detailansicht')
fig(ARTIFACTS[9],'Audit-Hash-Kette - Detailansicht')
story.append(PageBreak())
H2('A6 Anforderungs- und Testnachweis')
tab(req,'Anforderungsnachweis',widths=[13*mm,60*mm,29*mm,20*mm,34*mm],font=7.8)
fig(ARTIFACTS[13],'Traceability-Matrix - Detailansicht')
story.append(PageBreak())
H2('A7 Testprotokoll')
tab(tests,'Testprotokoll - Pilot / Evidenzstatus',widths=[10*mm,29*mm,54*mm,19*mm,25*mm,19*mm],font=6.6)
fig(ARTIFACTS[10],'Teststatus - Detailansicht')
story.append(PageBreak())
H2('A8 Abnahmevorlage')
accept=[['Prüfpunkt','Ergebnis','Nachweis / Bemerkung'],['Muss-Anforderungen erfüllt','[ ] ja  [ ] nein',''],['Testfälle nachvollziehbar','[ ] ja  [ ] nein',''],['Kritische Findings geschlossen','[ ] ja  [ ] nein',''],['Betriebs- und Datenschutzfreigabe','[ ] ja  [ ] nein',''],['Restmaßnahmen terminiert','[ ] ja  [ ] nein',''],['Pilot freigegeben','[ ] ja  [ ] nein','']]
tab(accept,'Abnahmecheckliste',widths=[65*mm,38*mm,53*mm])
P('Auftraggeber: zeichnungsberechtigte Vertretung des Projektbetriebs: __________________')
P('Datum: ____________________   Unterschrift: ______________________________')
callout('Diese Seite ist eine Vorlage. Unterzeichnen darf nur eine tatsächlich zeichnungs- oder entscheidungsberechtigte Vertretung des Projektbetriebs. Projektcoach und IHK-Prüfungsstelle ersetzen diese Rolle nicht automatisch.',risk=True)
story.append(PageBreak())
H2('A9 Budget- und Nachkalkulationsrahmen')
fig(ARTIFACTS[11],'Budgetrahmen - Detailansicht')
calc=[['Parameter','Wert / Status'],['Gesamtbudget laut Projektvorschlag','ca. 50.000 EUR'],['Budgetkategorien','Lizenzen, Schulung, externe Beratung'],['Persönlicher Prüfungsaufwand','70 aktive Stunden'],['Ist-Kosten','durch Angebote, Rechnungen und interne Verrechnungssätze zu ergänzen'],['Ist-Nutzen','nach Pilot anhand realer Prozessdaten zu messen'],['Break-even / ROI','erst nach belastbarer Nachkalkulation ausweisen']]
tab(calc,'Budget- und Nachkalkulationsdaten',widths=[85*mm,71*mm])
story.append(PageBreak())
H2('A10 Rollout-Roadmap')
fig(ARTIFACTS[12],'Rollout- und Skalierungsroadmap - Detailansicht')
P('Die Roadmap ist keine Freigabe für einen Produktivrollout. Jede Stufe erfordert eigene Eintritts- und Austrittskriterien sowie einen benannten Verantwortlichen.')
story.append(PageBreak())
H2('A11 Kick-off- und Gesprächsprotokoll - Vorlage')
proto=[['Feld','Inhalt'],['Projekt','Zero-Trust-Sicherheitskonzept mit GitHub-Integration'],['Ziel','technischer Pilot mit nachvollziehbarer Genehmigung, Provisioning und Audit'],['Teilnehmerrollen','[einzutragen: reale Teilnehmende, Funktionen und organisatorische Rollen]'],['Beschlüsse','Pilotabgrenzung, sechs Meilensteine, Repository als Projektakte, kritische Fehler blockieren Freigabe'],['Offene Punkte','betriebliche Owner, produktive SSO-Integration, Aufbewahrungsfrist, Abnahmeunterschrift'],['Protokollverantwortung','Daniel Massa, Projektleiter']]
tab(proto,'Kick-off-Protokoll',widths=[48*mm,108*mm],font=8.5)
callout('A11 ist eine Vorlage. Ohne reales Datum, realen Ort und externe Freigabe ist sie kein Nachweis eines durchgeführten Kick-offs.',risk=True)
P('Datum / Ort: noch offen - vor Abgabe mit realem Protokoll zu belegen')
P('Freigabe durch zeichnungsberechtigte Vertretung des Projektbetriebs: noch offen')
story.append(PageBreak())
H2('A12 Projektstatusbericht')
status2=[['Rubrik','Stand','Nächste Aktion','Verantwortung'],['Leistung','Pilot-Scope laut Projektunterlagen umgesetzt','Repository- und Betriebsnachweise final zuordnen','Projektleiter / Auftraggeber'],['Termin','Pilotdokumentation erstellt','Ist-Zeitnachweis finalisieren','Projektleiter'],['Kosten','Budgetrahmen ca. 50.000 EUR','Ist-Kosten aus Angeboten/Rechnungen nachführen','Projektleiter / Auftraggeber'],['Risiken','Fehlerstatus laut Unterlagen; reproduzierbarer Nachweis offen','Security- und Datenschutzfreigabe dokumentieren','IT / Compliance'],['Entscheidung','technischer Pilot beurteilbar','betriebliche Abnahme und Rolloutentscheidung','Auftraggeber']]
tab(status2,'Projektstatus zum Dokumentationsstichtag',widths=[34*mm,48*mm,49*mm,25*mm],font=7.8)
P('Gesamtstatus: GELB - Projektstammdaten und Planbasis bestätigt; Test-, Ist-Kosten- und Abnahmenachweise müssen der endgültigen Abgabefassung eindeutig zugeordnet werden.')

# build

doc=IHKDocTemplate(str(PDF_OUT),pagesize=A4,leftMargin=LEFT,rightMargin=RIGHT,topMargin=TOP,bottomMargin=BOTTOM,title='Zero-Trust-Sicherheitskonzept mit GitHub-Integration',author='Daniel Massa',subject='IHK-Projektarbeit - V13 interner 90-Punkte-Qualitätsgate-Kandidat')
doc.multiBuild(story)
print(PDF_OUT)
