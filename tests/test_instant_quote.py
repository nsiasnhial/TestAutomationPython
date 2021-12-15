"""
Tests For  Visx Catalog.
"""

from pages.HomePage import HomePage
from pages.PaymentPage import PaymentPage
from config import config_values
import pytest
import time
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestRentalCover(BaseTest):

    def test_title_rentalcover(self):
        self.homepage = HomePage(self.driver)
        title = self.homepage.getTitle()
        assert title == config_values.HOME_PAGE_TITLE

    def test_currenturl(self):
        assert self.driver.current_url == config_values.URL

    def test_get_instant_quote(self):
        self.homepage = HomePage(self.driver)
        self.paymentpage = PaymentPage(self.driver)

        self.homepage.selectCountryForQuote(config_values.COUNTRY)
        self.homepage.selectDatesForQuote()
        self.homepage.selectVehicle(config_values.VEHICLE_TYPE)
        self.homepage.getInstantQuote()

        self.paymentpage.verifyPolicyPaymentText()
        result = self.paymentpage.verifyPolicyInformation()
        assert result == True
        result = self.paymentpage.verifyAmountPresent()
        assert result ==True