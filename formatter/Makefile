SHELL=/bin/bash
.PHONY : init update build license header

build: license header ;

init : Pipfile
	pipenv install --dev --skip-lock

update : Pipfile
	pipenv update --dev
	pipenv lock -r > requirements-secure.txt
	pipenv lock -r --dev > requirements-secure-dev.txt
	pipenv run pip freeze > requirements.txt
	rm versioneer.py
	pipenv run versioneer install

license : Pipfile format.py ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-V1.1.html
	pipenv run ./format.py -m 3 --ascii ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-V1.1.html
	cp ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-V1.1.txt ../LICENSE

header : Pipfile format.py ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-HEADER-V1.1.html
	pipenv run ./format.py -w 72 --ascii ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-HEADER-V1.1.html
	cp ../cisco-sample-code-license/v1.1/CISCO-SAMPLE-CODE-LICENSE-HEADER-V1.1.txt ../HEADER
