import selenium
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import utilities.logger as cl
import logging


class LoginPage(SeleniumDriver):

    def __init(self, driver):
        super(LoginPage, self).__init(driver)
        self.driver = driver


     # Locators to be used against Main Shudder login page
    _login_link = "Login"
    _email = "//div[@class='input-row']//input[@id='email']"
    _password = "//div[@class='input-row']//input[@id='password']"
    _login_button = "//div[@class='button-row']//button"
    _invalidLoginMsg = "//div[@class='error-message']"


    ''' Basic actions'''
    def enterEmail(self, email):
        self.sendKeys(email, self._email, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password, locatorType="xpath")

    def clickLoginLink(self):
        self.elementClick(self._login_button, locatorType="xpath")



    ''' Functionality of Login Page '''
    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginLink()


    def verifyInvalidLogin(self):
        result = self.isElementPresent(self._invalidLoginMsg, locatorType="xpath")

        return result




