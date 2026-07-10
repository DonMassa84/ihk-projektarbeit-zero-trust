.PHONY: build gate v13 freeze clean status

build:   ## PDF bauen + Quality Gate (21 Seiten, Pandoc)
	python3 quality_gate/ihk_gate.py --build

gate:    ## Nur Quality Gate, ohne Build
	python3 quality_gate/ihk_gate.py

v13:     ## V13-Referenz-Build (63 Seiten, ReportLab)
	.venv-v13/bin/python3 tools/reference_build_v13.py

v13-venv:
	python3 -m venv .venv-v13
	.venv-v13/bin/pip install -r requirements-v13.txt

freeze:  ## SHA256-Freeze erzeugen
	bash quality_gate/freeze_release.sh

status:  ## Repository-Status anzeigen
	@echo "=== Git Log ==="
	@git log --oneline -5
	@echo ""
	@echo "=== Git Status ==="
	@git status --short
	@echo ""
	@echo "=== Quality Gate ==="
	@python3 quality_gate/ihk_gate.py 2>&1 | head -3

clean:
	rm -rf quality_gate/reports/* quality_gate/tmp/* quality_gate/rendered/*
