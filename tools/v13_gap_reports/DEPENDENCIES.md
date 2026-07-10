# V13 Build Dependencies

## Python Packages (`requirements-v13.txt`)

| Package    | Version  | Purpose                 |
|------------|----------|-------------------------|
| reportlab  | >= 4.0   | PDF generation          |
| matplotlib | >= 3.7   | Artifact diagrams       |
| Pillow     | >= 10.0  | Image handling          |
| pypdf      | >= 6.0   | PDF analysis/comparison |
| pymupdf    | >= 1.23  | PDF text extraction     |

## System Packages

| Package       | Purpose                | Install                       |
|---------------|------------------------|-------------------------------|
| poppler-utils | PDF→PNG rendering      | `apt install poppler-utils`   |
| python3-venv  | Virtual environment    | `apt install python3-venv`    |

## Tested Environment

- OS: Linux (Ubuntu 24.04)
- Python: 3.12
- reportlab: 5.0.0
- matplotlib: 3.11.0
- Pillow: 12.3.0
