"""
This class is the parent of all pages
It contains generic method and utilities for all the page class
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        return False

    def getElement(self, locator, locatorType="id"):
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    def getElements(self, locator, locatorType="id"):
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.driver.find_elements(byType, locator)
        return element

    def elementClick(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.click()

    def sendKeys(self, data, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        element.send_keys(data)


    def selectOptionByText(self, option, locator, locatorType="id"):
        self.waitForElementClickable(locator, locatorType)
        element = self.getElement(locator, locatorType)
        sel = Select(element)
        sel.select_by_visible_text(option)

    def waitForElement(self, locator, locatorType="id", timeout=10):
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((byType, locator)))
        return element

    def waitForElementClickable(self, locator, locatorType="id", timeout=10):
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((byType, locator)))
        return element

    def getText(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        return element.text

    def getTitle(self):
        return self.driver.title

    def getAttribute(self, locator, locatorType="id", attribute="value"):
        element = self.getElement(locator, locatorType)
        return element.get_attribute(attribute)

    def pageContainsText(self, text):
        return text in self.driver.page_source

    def isElementPresent(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        if element is not None:
            return True
        else:
            return False

    def maximizeWindow(self):
        self.driver.maximize_window()

    def refreshPage(self):
        self.driver.refresh()



