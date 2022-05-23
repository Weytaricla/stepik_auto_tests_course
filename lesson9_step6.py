from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser.get(link)

  button = browser.find_element_by_css_selector(".trollface")
  button.click()

  new_window = browser.window_handles[1]

  browser.switch_to.window(new_window)

  input_value = browser.find_element_by_css_selector("#input_value")
  num_value = int(input_value.text)
  result = calc(num_value)

  input = browser.find_element_by_css_selector("#answer")
  input.send_keys(result)

  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
    time.sleep(10)
    browser.quit()