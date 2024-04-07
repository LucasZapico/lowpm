all: main

main: 
	pipenv run python3 _main.py

build_bin:
	# todo: review how to roll this as single file
	pyinstaller --add-data ./.lowpm:.lowpm _main.py
	cp dist/_main/_main dist/_main/_internal/_main
	cp -r dist/_main/_internal/ dist/_internal
	rm -rf dist/_main
	cp -r dist/_internal/.lowpm dist/
	cp dist/_internal/_main dist/_main


dev:
	pipenv run python3 dev.py