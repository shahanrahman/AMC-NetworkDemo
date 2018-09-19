import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest
import os
from pages.home.login_page import LoginPage
from pages.home.member_page import MembersPage
import time
import utilities.logger as cl
import logging



class LoginTests(unittest.TestCase):

    BaseURL = "https://www.shudder.com/login"
    driverLocation = "C:\\Users\shaha\\PycharmProjects\\lib\\Chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(BaseURL)

    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("shahan.rahman1211@gmail.com", "Gettrial123")
        time.sleep(5)


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.BaseURL)
        self.lp.login("shaef@gmail.com", "wrongPass")
        result = self.lp.verifyInvalidLogin()
        time.sleep(5)
        assert result == True










