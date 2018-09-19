import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from base.selenium_driver import SeleniumDriver
import utilities.logger as cl
import logging
import time


class searchShudder(SeleniumDriver):

    def __init(self, driver):
        super(searchShudder, self).__init(driver)
        self.driver = driver

    #Search Feture Locators

    _searchLink ="//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[5]"
    _searchShudder ="//input[@class='search-input']"
    _exitSearch = "//div[@class='search-close']"

    #List Of Movie Tittle Locators

    _getNumOfResults = "//div[@class='search-results'] //div[1]"
    _movieDisplayed01 = "//div[@class='search-results-list'] //div[1]//a//div//span"
    _movieDisplayed02 = "//div[@class='search-results-list'] //div[2]//a//div//span"
    _movieDisplayed03 = "//div[@class='search-results-list'] //div[3]//a//div//span"
    _movieDisplayed04 = "//div[@class='search-results-list'] //div[4]//a//div//span"



    #actions
    def selectToSearch(self):
        self.elementClick(self._searchLink, locatorType="xpath")

    def searchShudder(self, data):
        self.sendKeys(data, self._searchShudder, locatorType="xpath")

    def exitSearch(self):
        self.elementClick(self._searchLink, locatorType="xpath")

    def selectMovie01(self):
        self.elementClick(self._movieDisplayed01, locatorType="xpath")
        self.getElement(self._movieDisplayed01, locatorType="xpath").text()

    def selectMovie02(self):
        self.elementClick(self._movieDisplayed02, locatorType="xpath")
        print self.getElement(self._movieDisplayed02, locatorType="xpath")

    def selectMovie03(self):
        self.elementClick(self._movieDisplayed03, locatorType="xpath")
        self.getElement(self._movieDisplayed03, locatorType="xpath").text()

    def selectMovie04(self):
        self.elementClick(self._movieDisplayed04, locatorType="xpath")
        self.getElement(self._movieDisplayed04, locatorType="xpath").text()



    def searchShudder(self, data):
        self.selectToSearch()
        self.searchShudder("dead")
        self.selectMovie02()
        



