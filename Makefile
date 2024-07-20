VENV_BIN = ./.venv/bin

venv:
	python -m venv .venv

resume:
	$(VENV_BIN)/python ./generate.py

.PHONY: dev
dev:
	$(VENV_BIN)/python -m http.server & ./dev/watch_generate.sh

.PHONY: test
test:
	$(VENV_BIN)/pytest

.PHONY: install-dependencies
install-dependencies:
	$(VENV_BIN)/pip install -r requirements.txt
