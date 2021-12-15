from selenium.webdriver.common.by import By
import selenium.webdriver
import pytest

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = selenium.webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()
