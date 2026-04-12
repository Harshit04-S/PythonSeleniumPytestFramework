
import time
from selenium.webdriver.common.by import By



def test_sort(browserInstance):
    driver = browserInstance
    browserSortedList = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    fruitList = driver.find_elements(By.XPATH, "//tr/td[1]")

    for fruit in fruitList:
        browserSortedList.append(fruit.text)

    print(browserSortedList)

    varList = browserSortedList.copy()

    browserSortedList.sort()
    print(browserSortedList)

    assert varList == browserSortedList

    time.sleep(4)