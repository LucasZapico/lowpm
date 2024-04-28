all: main

main: 
	pipenv run python3 _main.py

build_bin:
	# todo: review how to roll this as single file
	pyinstaller --onefile --hidden-import=yaml _main.py
	cp -r .lowpm dist/.lowpm

dev:
	pipenv run python3 dev.py