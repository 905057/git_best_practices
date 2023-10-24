all: style-check type-check unittest test
	@echo "All done..."

unittest:
	pytest -v test_hvertskalmaeta.py
	
test:
	@cat 1.in | python hvertskalmaeta.py | diff - 1.ans
	@cat 2.in | python hvertskalmaeta.py | diff - 2.ans
	@echo "All local test passed..."

style-check:
	flake8 .

style-fix:
	autopep8 --in-place --recursive --aggressive --aggressive .

type-check:
	mypy --strict .

kattis:
	@kattis -f hvertskalmaeta.py