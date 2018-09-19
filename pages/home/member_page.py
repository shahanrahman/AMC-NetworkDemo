import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from base.selenium_driver import SeleniumDriver
import utilities.logger as cl
import logging
import time


class MembersPage(SeleniumDriver):

    def __init(self, driver):
        super(MembersPage, self).__init(driver)
        self.driver = driver

    #Main Header Locators

    _shudderIcon = "//header[@id='header']//div[@class='container']/div[@id='header__logo']"
    _collectionsLink = "//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[1]"
    _moviesLink = "//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[2]"
    _seriesLink = "//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[3]"
    _shudderTVLink = "//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[4]"
    _searchLink ="//header[@id='header']//div[@class='container']/nav[@id='header__menu']//ul//li[5]"
    _searchShudder ="//input[@class='search-input']"
    _myAccountLink = "//div[@id='header__user__account']"


    ''' Actions Created to navigate throughout the main header links'''

    def navigateBackToMembersPage(self):
        self.elementClick(self._shudderIcon, locatorType='xpath')

    def navigateToCollections(self):
        self.elementClick(self._collectionsLink, locatorType="xpath")


    def navigateToMovies(self):
        self.elementClick(self._moviesLink, locatorType="xpath")


    def navigateToSeries(self):
        self.elementClick(self._seriesLink, locatorType="xpath")


    def navigateToShudderTV(self):
        self.elementClick(self._shudderTVLink, locatorType="xpath")


    def selectToSearch(self):
        self.elementClick(self._searchLink, locatorType="xpath")


    def searchShudder(self, data):
        self.sendKeys(data, self._searchShudder, locatorType="xpath")


    def navigateToMyAccount(self):
        self.elementClick(self._myAccountLink, locatorType="xpath")


    '''Functionality of Main Header'''

    def headerVerification(self):
        self.navigateToCollections()
        self.navigateToMovies()
        self.navigateToSeries()
        self.navigateToShudderTV()
        #self.selectToSearch()
        #self.searchShudder(data)









