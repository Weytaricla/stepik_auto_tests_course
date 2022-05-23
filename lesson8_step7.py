from selenium import webdriver
import time
import math

def calc(x): 
  return str(math.log(abs(12*math.sin(x)))) #log/ln?

try:
  browser = webdriver.Chrome()
  link = "http://SunInJuly.github.io/execute_script.html"
  browser.get(link)

  x_element = browser.find_element_by_css_selector("#input_value")
  x = int(x_element.text)
  y = calc(x)

  #answer
  input = browser.find_element_by_css_selector("#answer")
  input.send_keys(y)

  #checkbox
  checkbox = browser.find_element_by_css_selector("#robotCheckbox")
  checkbox.click()
  #radio
  radio = browser.find_element_by_css_selector("#robotsRule")
  #scroll
  browser.execute_script("return arguments[0].scrollIntoView(true)", radio)
  radio.click()

  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
    time.sleep(10)
    browser.quit()