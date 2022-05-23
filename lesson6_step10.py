from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_css_selector(".first_block input")
    for element in elements:
        element.send_keys("answer")

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