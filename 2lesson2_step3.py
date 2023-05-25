from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.CSS_SELECTOR,'#num1')
    b = browser.find_element(By.CSS_SELECTOR,'#num2')
    a_num = a.text
    b_num = b.text
    x = int(a_num) + int(b_num)
    print(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))
    but_submit = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    but_submit.click()

finally:
    time.sleep(30)
    browser.quit()