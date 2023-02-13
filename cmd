# Libraries required for installation:
pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager


# We run tests one by one:
behave -f html -o behave-report.html --tags=cart_price
behave -f html -o behave-report.html --tags=cart_remove
behave -f html -o behave-report.html --tags=favorites
behave -f html -o behave-report.html --tags=login_test
behave -f html -o behave-report.html --tags=login_buy
behave -f html -o behave-report.html --tags=search
behave -f html -o behave-report.html --tags=search_with_filter

# We run full test:
behave -f html -o behave-report.html