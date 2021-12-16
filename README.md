# Setup Instructions

## Python Setup

Test can be set up on macOS.

Python Version: Python 3.8 or higher.
Download the latest Python version from [Python.org](https://www.python.org/downloads/).

To install pipenv, run `pip install pipenv` from the command line.

Python editor/IDE: PyCharm

## WebDriver Setup

For Web UI testing, download and install the latest versions of the WebDriver executables
for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

Use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).


To install ChromeDriver and geckodriver on macOS
simply move them from downloaded path to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

### Test WebDriver Setup

To verify correct setup, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

verify that you can run them without errors.
Use Ctrl-C to kill them.

## Framework Setup
1. Make the Framework directory
2. Run `cd TestAutomationPython` to enter the project directory
3. Run `pipenv install virtualenv` to create virtual environment
4. Run `pipenv  install selenium` to install selenium
5. Run `pipenv  install pytest` to install pytest package
6. Run `pip install pytest-html` to install pytest html plugin for reports


Run `pipenv run python -m pytest` to verify that the framework can run tests.

### Running Test
1. Run a specific test:
```
pipenv run python -m pytest -v tests/test_instant_quote.py -s
```
2. Run a specific test  and generate report:
```
pipenv run python -m pytest -v tests/test_instant_quote.py -s --html=reports/test_report.html
```

## Project Setup after clone the repository

1. Clone this repository.
2. Run `cd visx-ui-test` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. (Please do not run this command as this will run ALL the tests and they need fixing)

Run `pipenv run python -m pytest` to verify that the framework can run tests.

### Running Test
1. Run a specific test:
```
pipenv run python -m pytest -v tests/test_instant_quote.py -s
```
2. Run a specific test is a given browser and report:
```
pipenv run python -m pytest -v tests/test_instant_quote.py -s --html=reports/test_report.html
```



## Test Details and Assumptions
1. Enter the following data to get the instant quote:
    a. Country: United States
    b. From/To dates: one day future date
    c. Car/vehicle type: Car



