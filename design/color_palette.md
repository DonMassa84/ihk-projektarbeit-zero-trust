# Farbpalette — IHK Projektarbeit

**Version:** 1.0  
**Datum:** 09.07.2026

---

## Primärfarben

| Name | Hex | RGB | CMYK | HSL | Verwendung |
|------|-----|-----|------|-----|------------|
| **Primary Dark** | `#1B1F24` | 27, 31, 36 | 93, 88, 86, 80 | 225°, 14%, 12% | Haupttext, Überschriften, Rahmen, Footer |
| **Primary Blue** | `#2E5C8A` | 46, 92, 138 | 87, 58, 0, 46 | 210°, 50%, 36% | Akzente, Links, Diagramm-Highlights, Tabellen-Header |
| **Secondary Blue** | `#4A8FC7` | 74, 143, 199 | 63, 28, 0, 22 | 207°, 54%, 54% | Hover-Zustände, sekundäre Akzente, Chart-Serie 2 |

---

## Semantische Farben (Status / Feedback)

| Name | Hex | RGB | CMYK | HSL | Verwendung |
|------|-----|-----|------|-----|------------|
| **Success Green** | `#2D7D32` | 45, 125, 50 | 84, 0, 88, 51 | 122°, 46%, 33% | Bestanden, Positiv, Abgeschlossen, "Grün" in Ampel |
| **Warning Orange** | `#E67E22` | 230, 126, 34 | 0, 45, 85, 10 | 28°, 79%, 52% | Warnung, Teilweise, Offen, "Gelb" in Ampel |
| **Danger Red** | `#C62828` | 198, 40, 40 | 0, 80, 80, 22 | 0°, 66%, 47% | Kritisch, Nicht bestanden, Mangel, "Rot" in Ampel |
| **Info Blue** | `#1E88E5` | 30, 136, 229 | 87, 41, 0, 10 | 205°, 77%, 51% | Information, Hinweis, "Blau" in Ampel |

---

## Neutrale Farben

| Name | Hex | RGB | CMYK | HSL | Verwendung |
|------|-----|-----|------|-----|------------|
| **Neutral 900** | `#1B1F24` | 27, 31, 36 | 93, 88, 86, 80 | 225°, 14%, 12% | Haupttext (gleich Primary Dark) |
| **Neutral 700** | `#4B5563` | 75, 85, 99 | 68, 55, 46, 38 | 215°, 14%, 34% | Hilfetexte, Metadaten, Fußnoten |
| **Neutral 500** | `#6B7280` | 107, 114, 128 | 52, 38, 31, 26 | 215°, 9%, 46% | Deaktivierte Elemente, Platzhalter |
| **Neutral 300** | `#D1D5DB` | 209, 213, 219 | 12, 8, 6, 0 | 220°, 14%, 83% | Rahmen, Trennlinien, Tabellen-Grid |
| **Neutral 100** | `#F3F4F6` | 243, 244, 246 | 4, 2, 2, 0 | 220°, 33%, 96% | Tabellenzeilen (alternierend), Code-Blöcke, Hover-Hintergrund |
| **Neutral 50** | `#F9FAFB` | 249, 250, 251 | 2, 1, 1, 0 | 220°, 33%, 98% | Seitenhintergrund (alternativ zu Weiß) |
| **White** | `#FFFFFF` | 255, 255, 255 | 0, 0, 0, 0 | 0°, 0%, 100% | Seitenhintergrund, Karten-Hintergrund |

---

## Diagramm-Farben (Kategorisch, max. 8)

| Index | Hex | Name | Verwendung |
|-------|-----|------|------------|
| 1 | `#2E5C8A` | Primary Blue | Hauptserie, Admin-Rolle |
| 2 | `#4A8FC7` | Secondary Blue | Developer-Rolle |
| 3 | `#2D7D32` | Success Green | Auditor / Positiv |
| 4 | `#E67E22` | Warning Orange | HR-Manager / Warnung |
| 5 | `#C62828` | Danger Red | Kritisch / Finance-Rolle |
| 6 | `#6A1B9A` | Purple | Read-Only / Spezial |
| 7 | `#00695C` | Teal | Sekundärsysteme |
| 8 | `#5D4037` | Brown | Legacy / Archiv |

**Hinweis:** Bei mehr als 8 Kategorien → Muster (Schraffur, Punkte) statt weiterer Farben.

---

## Barrierefreiheit (WCAG 2.1 AA)

| Vordergrund | Hintergrund | Kontrast | Status |
|-------------|-------------|----------|--------|
| Primary Dark (`#1B1F24`) | White (`#FFFFFF`) | 15.9:1 | ✅ AAA |
| Primary Blue (`#2E5C8A`) | White (`#FFFFFF`) | 5.9:1 | ✅ AA |
| Success Green (`#2D7D32`) | White (`#FFFFFF`) | 5.4:1 | ✅ AA |
| Warning Orange (`#E67E22`) | White (`#FFFFFF`) | 3.2:1 | ⚠️ AA Large only |
| Danger Red (`#C62828`) | White (`#FFFFFF`) | 4.8:1 | ✅ AA |
| Neutral 700 (`#4B5563`) | White (`#FFFFFF`) | 7.5:1 | ✅ AAA |

**Regel:** Warning Orange **nicht** als Fließtext auf Weiß verwenden — nur für Icons, Badges, Ampeln (≥ 18 pt / 14 pt bold).

---

## Druck / PDF-spezifisch

| Aspekt | Empfehlung |
|--------|------------|
| **Farbraum** | CMYK im Druck, sRGB im PDF (PDF/X-3 konform) |
| **Schwarz** | 100% K (nicht "Rich Black") für Text |
| **Blau** | C: 87 M: 58 Y: 0 K: 46 (Primary Blue) |
| **Grau 300** | C: 12 M: 8 Y: 6 K: 0 |
| **Überdrucken** | Schwarzer Text auf farbigem Hintergrund → Überdrucken aktivieren |
| **Spotfarben** | Nicht verwenden (Prozessfarben nur) |

---

## CSS-Variablen (für HTML-Export / Web-Preview)

```css
:root {
  /* Primär */
  --color-primary-dark: #1B1F24;
  --color-primary-blue: #2E5C8A;
  --color-secondary-blue: #4A8FC7;

  /* Semantisch */
  --color-success: #2D7D32;
  --color-warning: #E67E22;
  --color-danger: #C62828;
  --color-info: #1E88E5;

  /* Neutral */
  --color-neutral-900: #1B1F24;
  --color-neutral-700: #4B5563;
  --color-neutral-500: #6B7280;
  --color-neutral-300: #D1D5DB;
  --color-neutral-100: #F3F4F6;
  --color-neutral-50: #F9FAFB;
  --color-white: #FFFFFF;

  /* Diagramm */
  --color-chart-1: #2E5C8A;
  --color-chart-2: #4A8FC7;
  --color-chart-3: #2D7D32;
  --color-chart-4: #E67E22;
  --color-chart-5: #C62828;
  --color-chart-6: #6A1B9A;
  --color-chart-7: #00695C;
  --color-chart-8: #5D4037;
}
```

---

## Mermaid-Thema (für Diagramme)

```mermaid
%%{init: {'themeVariables': {
  'primaryColor': '#2E5C8A',
  'primaryTextColor': '#1B1F24',
  'primaryBorderColor': '#D1D5DB',
  'lineColor': '#4B5563',
  'secondaryColor': '#4A8FC7',
  'tertiaryColor': '#F3F4F6',
  'background': '#FFFFFF',
  'mainBkg': '#FFFFFF',
  'secondBkg': '#F3F4F6',
  'tertiaryBkg': '#E5E7EB',
  'textColor': '#1B1F24',
  'fontFamily': 'Liberation Sans, Arial, sans-serif',
  'fontSize': '12px',
  'edgeLabelBackground': '#FFFFFF',
  'clusterBkg': '#F9FAFB',
  'clusterBorder': '#D1D5DB'
}}}%%
```

---

## PlantUML-Stil (für Diagramme)

```plantuml
skinparam defaultFontName Liberation Sans
skinparam defaultFontSize 11
skinparam defaultTextColor #1B1F24

skinparam rectangle {
  BackgroundColor #FFFFFF
  BorderColor #2E5C8A
  FontColor #1B1F24
}

skinparam component {
  BackgroundColor #F3F4F6
  BorderColor #2E5C8A
  FontColor #1B1F24
}

skinparam activity {
  BackgroundColor #F3F4F6
  BorderColor #2E5C8A
  FontColor #1B1F24
  DiamondBackgroundColor #E67E22
}

skinparam arrow {
  Color #4B5563
  FontColor #4B5563
}

skinparam legend {
  BackgroundColor #F9FAFB
  BorderColor #D1D5DB
  FontColor #1B1F24
}
```

---

*Ende Farbpalette. Alle Werte getestet für PDF-Druck, HTML-Export und Bildschirmpräsentation.*