"""
This is the class for PaymentPage ie
using Page Object Model for the rentalcover application
"""

from pages.BasePage import BasePage
from config import config_values

class PaymentPage(BasePage):

    # Locators
    policy_information = "//h2[@id='policy-inclusions']"
    destination = "//body/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]"
    vehicle = "//body[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]"
    amount = "//body/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[3]"


    # Initializer
    def __init__(self, driver):
        super().__init__(driver)

    # Interaction Methods for the page class PaymentPage



    # Functions

    def getPolicyInformationText(self):
        policy_text = self.getText(self.policy_information, locatorType="xpath")
        return policy_text

    def getDestination(self):
        country = self.getText(self.destination, locatorType="xpath")
        return country

    def getVehicle(self):
        v = self.getText(self.vehicle, locatorType="xpath")
        return v


    # Calling Functions

    def verifyPolicyInformation(self):
        result = self.isElementPresent(self.policy_information, locatorType="xpath")
        return result

    def verifyAmountPresent(self):
        result = self.isElementPresent(self.amount, locatorType="xpath")
        return result

    def verifyPolicyPaymentText(self):
        policy_text = self.getPolicyInformationText()
        assert policy_text == config_values.POLICY_INFO_TEXT
        country = self.getDestination()
        assert country == config_values.COUNTRY
        vehi = self.getVehicle()
        assert vehi == config_values.VEHICLE_TYPE
