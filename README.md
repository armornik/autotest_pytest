# selenium_auto"

## For work with file need
1. pip install requirements.txt
2. Download driver for browser from: https://sites.google.com/a/chromium.org/chromedriver/downloads
3.1.1. Unzip file in C:\chromedriver (for Windows)
3.1.2. Add Path in System variables  C:\chromedriver
3.2. In IDE add unzip file in \environments\our_env\Scripts\
   
Useful Pytest commands: https://gist.github.com/amatellanes/12136508b816469678c2

## Run browser Firefox:
1. Download driver for browser from: https://github.com/mozilla/geckodriver/releases
2. Copy file in: \PycharmProjects\selenium_first\env\Scripts
3. Create file conftest.py:
   import pytest
    from selenium import webdriver
   
    def pytest_addoption(parser):
        parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
4. Run file with command: pytest -s -v --browser_name=firefox test_name_file.py

## List plugin for PyTest:
https://docs.pytest.org/en/latest/reference/plugin_list.html

## Rerun test:
1. pip install pytest-rerunfailures
2. Add param "--reruns n"
3. pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
4. Param --tb=line - small traceback. https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing 
