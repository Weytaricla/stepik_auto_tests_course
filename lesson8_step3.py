from selenium import webdriver
from selenium.webdriver.support.ui import Select #import select
import time
import math

def calc(x, y):
  x = int(x)
  y = int(y)
  return str(x + y)

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_num_element = browser.find_element_by_css_selector("#num1")
    first_num = first_num_element.text

    second_num_element = browser.find_element_by_css_selector("#num2")
    second_num = second_num_element.text


    sum = calc(first_num, second_num)

    select = Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()