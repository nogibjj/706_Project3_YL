install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
 	# black *.py

lint:
 	# ruff check *.py mylib/*.py

test:
 	# python -m pytest -vv --cov=mylib test_*.py

job:
    python trigger.py