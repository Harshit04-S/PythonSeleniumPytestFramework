import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from PageObjects.login import LoginPage
from PageObjects.shopPage import ShopPage

# for reading data from json data file
test_data_path = '../Data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)         # test_data: python object
    test_list = test_data["data"]
    print(test_list)

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):

    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()

