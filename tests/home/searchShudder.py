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
from pages.home.searchAndLocate import searchShudder



class searchShudder(unittest.TestCase):

    BaseURL = "https://www.shudder.com/login"
    driverLocation = "C:\\Users\shaha\\PycharmProjects\\lib\\Chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(BaseURL)

    lp = LoginPage()
    mp = MembersPage()
    ss = searchShudder()


    def searchForMovie(self):
        self.lp.login("shahan.rahman1211@gmail.com", "Gettrial123")
        time.sleep(5)
        self.mp.headerVerification()
        time.sleep(5)
        self.ss.searchShudder("dead")
        time.sleep(5)
