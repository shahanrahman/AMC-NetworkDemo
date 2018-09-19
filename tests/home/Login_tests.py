from selenium import webdriver
import unittest
import pytest
import os
from pages.home.login_page import LoginPage
import time



class LoginTests(unittest.TestCase):

    BaseURL = "https://www.shudder.com/login"
    driverLocation = "C:\\Users\shaha\\PycharmProjects\\lib\\Chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(BaseURL)

    lp = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):

        self.lp.login("shahan.rahman1211@gmail.com", "Gettrial123")
        time.sleep(5)


    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        self.driver.get(self.BaseURL)
        self.lp.login("shaef@gmail.com", "wrongPass")
        result = self.lp.verifyInvalidLogin()
        assert result == True















