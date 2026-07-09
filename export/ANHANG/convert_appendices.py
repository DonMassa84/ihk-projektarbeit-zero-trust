import weasyprint
import os
import glob

css = weasyprint.CSS(string="""
@page { size: A4; margin: 2.5cm; }
body { font-family: Liberation Sans, Arial, sans-serif; font-size: 11pt; line-height: 1.5; margin: 0; }
h1 { color: #1B1F24; border-bottom: 2px solid #2E5C8A; padding-bottom: 4pt; margin-top: 0; }
h2 { color: #1B1F24; margin-top: 18pt; }
h3 { color: #2E5C8A; }
code { background: #F3F4F6; padding: 2pt 4pt; border-radius: 3pt; font-family: Liberation Mono, monospace; }
pre { background: #F8F9FA; border: 1px solid #D1D5DB; padding: 8pt; overflow-x: auto; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; margin: 12pt 0; font-size: 10pt; }
th, td { border: 0.5pt solid #D1D5DB; padding: 4pt 8pt; }
th { background: #EFF3F7; text-align: left; }
blockquote { border-left: 3px solid #2E5C8A; padding-left: 12pt; color: #4B5563; font-style: italic; }
""")

for f in glob.glob("*.md"):
    base = os.path.splitext(f)[0]
    content = open(f).read()
    weasyprint.HTML(string=content).write_pdf(base + ".pdf", stylesheets=[css])
    print(f"Created {base}.pdf")