from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:

  browser = webdriver.Chrome()
  browser.implicitly_wait(5)

  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # button = WebDriverWait(browser, 12).until(
  #   EC.element_to_be_clickable((By.ID, "book"))
  # ) 
  # button.click()

  price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )

  button = browser.find_element_by_css_selector("#book")
  button.click()

  input_value = browser.find_element_by_css_selector("#input_value")
  num_value = int(input_value.text)
  result = calc(num_value)

  input = browser.find_element_by_css_selector("#answer")
  input.send_keys(result)

  submit_button = browser.find_element_by_css_selector("#solve")
  submit_button.click()

finally:
    time.sleep(10)
    browser.quit()