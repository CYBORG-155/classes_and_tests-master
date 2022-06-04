test:
	pytest --cov=models --cov-report term-missing

install:
	pip install -r requirements.txt