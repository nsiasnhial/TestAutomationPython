"""
This is the class for HomePage ie
using Page Object Model for the rentalcover application
"""

from datetime import timedelta, datetime
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from config import config_values
import time


class HomePage(BasePage):

    # Locators
    country_field = "//input[@class='QuoteForm-destination-select form-control ui-autocomplete-input Field-input']"
    fromdate_field = "QuoteForm_FromDate-datepicker"
    todate_field = "QuoteForm_ToDate-datepicker"
    vehicle_change_lnk = "//body[1]/section[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/a[1]/strong[1]"

    vehicle_type_select = "//select[@id='QuoteForm_VehicleType']"
    get_quote_btn = "//button[@class='QuoteForm-submit Form-submit btn btn-warning btn-lg btn-block']"

    first_month_table = "//body/div[@id='ui-datepicker-div']/div[2]/table[1]"
    second_month_table = "//body/div[@id='ui-datepicker-div']/div[3]/table[1]"

    # Initializer
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(config_values.URL)

    # Interaction Methods for the page class HomePage

    def enterCountry(self, countryName):
        self.sendKeys(countryName, self.country_field, locatorType="xpath")

    def clickFromDate(self):
        self.elementClick(self.fromdate_field, locatorType="id")

    def clickToDate(self):
        self.elementClick(self.todate_field, locatorType="id")

    def clickVehicleChangeLnk(self):
        self.elementClick(self.vehicle_change_lnk, locatorType="xpath")

    def selectVehicleType(self, option):
        self.selectOptionByText(option, self.vehicle_type_select, locatorType="xpath")

    def clickGetQuoteBtn(self):
        self.elementClick(self.get_quote_btn, locatorType="xpath")

    # Functions

    def getFirstMonthTable(self):
        firstMonthTable = self.getElement(self.first_month_table, locatorType="xpath")
        return firstMonthTable

    def getSecondMonthTable(self):
        secondMonthTable = self.getElement(self.second_month_table, locatorType="xpath")
        return secondMonthTable

    def getPageTitle(self):
        return self.getTitle()

    ''' This method is used to get the attribute for fromdate field'''
    def getAttributeForFromDate(self):
        date_value = self.getAttribute(self.fromdate_field, locatorType="id", attribute="data-default-value")
        return date_value

    ''' This method is used to get the attribute for todate field'''
    def getAttributeForToDate(self):
        date_value = self.getAttribute(self.todate_field, locatorType="id", attribute="data-default-value")
        return date_value

    ''' This method is used to convert the date from string to date time format'''
    def getFromDate(self):
        from_date_value = self.getAttributeForFromDate()
        from_date = datetime.strptime(from_date_value, "%Y-%m-%d")
        return from_date

    def getToDate(self):
        to_date_value = self.getAttributeForToDate()
        to_date = datetime.strptime(to_date_value, "%Y-%m-%d")
        return to_date

    ''' This method is used to calculate the future date
         Here the assumption to take the next day so adding 
         days=1 with the date value'''
    def calculateFutureDate(self, dateValue):
        future_date = dateValue + timedelta(days=1)
        future_days = future_date.day
        return future_days



    ''' This method is used to select future date for fromdate'''
    def selectFutureDateForFromDate(self):
        from_date = self.getFromDate()
        from_days = from_date.day
        future_days = self.calculateFutureDate(from_date)
        self.clickFromDate()
        if future_days > from_days:
            first_month_table = self.getFirstMonthTable()
            dates = first_month_table.find_elements(By.TAG_NAME, "a")
            for d in dates:
                if d.text == str(future_days):
                    d.click()
                    break
        else:
            second_month_table = self.getSecondMonthTable()
            dates = second_month_table.find_elements(By.TAG_NAME, "a")
            for d in dates:
                if d.text == str(future_days):
                    d.click()
                    break

    ''' This method is used to select future date for fromdate'''
    def selectFutureDateForToDate(self):
        to_date = self.getToDate()
        to_days = to_date.day
        future_days = self.calculateFutureDate(to_date)
        self.clickToDate()
        if future_days > to_days:
            first_month_table = self.getFirstMonthTable()
            dates = first_month_table.find_elements(By.TAG_NAME, "a")
            for d in dates:
                if d.text == str(future_days):
                    d.click()
                    break
        else:
            second_month_table = self.getSecondMonthTable()
            dates = second_month_table.find_elements(By.TAG_NAME, "a")
            for d in dates:
                if d.text == str(future_days):
                    d.click()
                    break

    # Calling Functions

    def selectCountryForQuote(self, country):
        self.enterCountry(country)

    def selectDatesForQuote(self):
        self.selectFutureDateForFromDate()
        self.selectFutureDateForToDate()

    def selectVehicle(self, vehicle):
        self.clickVehicleChangeLnk()
        self.selectVehicleType(vehicle)

    def getInstantQuote(self):
        self.clickGetQuoteBtn()



















