from selenium import webdriver
import time
import math
import os


try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/file_input.html"
  browser.get(link)

  firstname = browser.find_element_by_css_selector("[name=firstname]")
  firstname.send_keys("firsdtname")

  lastname = browser.find_element_by_css_selector("[name=lastname]")
  lastname.send_keys("lastname")

  email = browser.find_element_by_css_selector("[name=email]")
  email.send_keys("email")

  current_dir = os.path.abspath(os.path.dirname(__file__)) #way to directory
  file_path = os.path.join(current_dir, 'file.txt') #take file

  file = browser.find_element_by_css_selector("[name=file]")
  file.send_keys(file_path)

  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
    time.sleep(10)
    browser.quit()