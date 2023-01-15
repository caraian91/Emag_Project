Libraries
pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

Run test
behave -f html -o behave-report.html --tags=emag
behave -f html -o behave-report.html --tags=favorites