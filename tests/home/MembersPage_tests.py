import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
from pages.home.login_page import LoginPage
from pages.home.member_page import MembersPage
import time
import utilities.logger as cl
import logging


class membersPageVerification(unittest.TestCase):

    def test_validLogin(self):

        BaseURL = "https://www.shudder.com/login"
        driverLocation = "C:\\Users\shaha\\PycharmProjects\\lib\\Chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(BaseURL)

        lp = LoginPage(driver)
        lp.login("shahan.rahman1211@gmail.com", "Gettrial123")
        time.sleep(10)
        mp = MembersPage(driver)
        mp.headerVerification("Texas")
        time.sleep(15)