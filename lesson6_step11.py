from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector(".first_block .first")
    input_name.send_keys("name")
    input_last_name = browser.find_element_by_css_selector(".first_block .second")
    input_last_name.send_keys("last_name")
    input_email = browser.find_element_by_css_selector(".first_block .third")
    input_email.send_keys("email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    #Text on page
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    #Запись в переменную текста
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()