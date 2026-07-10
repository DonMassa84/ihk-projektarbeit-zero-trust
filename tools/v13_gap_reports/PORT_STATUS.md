# V13 Port Status

## Summary

| Item                      | Status |
|---------------------------|--------|
| Script ported             | ✅ `tools/reference_build_v13.py` |
| Assets extracted          | ✅ `08_assets/v13/` (16 images + cover) |
| Output directory          | ✅ `09_export/reference_v13/` |
| Local build               | ✅ Exit code 0 |
| PDF pages                 | ✅ 63 pages |
| Page size                 | ✅ A4 (595 x 842 pt) |
| Not encrypted             | ✅ |
| Text vs reference         | ✅ 100% identical (0 text diffs across 63 pages) |
| Visual pixel diff         | ⚠️ 22 pages with pixel differences (expected – library version diffs) |
| SHA256 match              | ❌ Not expected (metadata differs: creation date, producer version) |

## Files Created

- `tools/reference_build_v13.py` – ported build script (repo-relative paths)
- `08_assets/v13/` – 14 artifact PNGs + cover_engine.png + source_cover.png
- `09_export/reference_v13/` – local PDF + reference PDF from package
- `requirements-v13.txt` – Python dependencies
- `99_reports/v13_port/` – this report + comparison results

## Build Command

```bash
# Create venv (one-time)
python3 -m venv .venv-v13
source .venv-v13/bin/activate
pip install -r requirements-v13.txt

# Build
MPLBACKEND=Agg python3 tools/reference_build_v13.py

# Expected output:
# 09_export/reference_v13/PROJEKTARBEIT_ZERO_TRUST_IHK_V13_90_GATE.pdf
```
