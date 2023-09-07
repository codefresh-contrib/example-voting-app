import os
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    InvalidSelectorException,
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotInteractableException,
    WebDriverException)

vote_endpoint = os.getenv('VOTE_ENDPOINT')
result_endpoint = os.getenv('RESULT_ENDPOINT')

@pytest.fixture(scope='module')

def browser():   
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Remote(
        command_executor='http://selenium-router:4444/wd/hub',
        options=chrome_options
    )
    
    yield browser
    browser.quit()


def test_confirm_result_title(browser):
    browser.get("http://{}".format(result_endpoint))
    assert "Cats vs Dogs -- Result" in browser.title


def test_confirm_result(browser):
    browser.get("http://{}".format(result_endpoint))
    element = browser.find_element(By.ID, 'result')
    assert element.get_attribute('id') == 'result'
