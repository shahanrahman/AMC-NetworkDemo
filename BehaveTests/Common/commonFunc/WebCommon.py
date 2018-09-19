import selenium
from selenium import webdriver

def go_to (url, browser_type = None):

    if not browser_type:
        driver = webdriver.Chrome()
    elif browser_type.lower() == 'chrome':

        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    url = url.strip()
    driver.get(url)

    return driver
