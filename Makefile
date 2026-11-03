.PHONY: install test lint run

install:
	python -m pip install -r requirements-dev.txt

test:
	pytest -v

lint:
	ruff check .

run:
	uvicorn app.main:app --reload
