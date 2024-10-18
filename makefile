install:
	pip3 install -r requirements.txt
run:
	PYTHONPATH=${PWD} python3 ./src/main.py