from email import message
from xml.dom.minidom import Document
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from array import *
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
class TestParams():

    global msg
    msg = str('') #for writing pieces of messages from pages

    links_array = array('i',[
        236895,
        236896,
        236897,
        236898,
        236899,
        236903,
        236904,
        236905
    ])
    
    @pytest.mark.parametrize('links', links_array)
    def test_page1(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)

        browser.implicitly_wait(10) #Ждём пока найдётся элемент
        textarea = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")

        answer = str(math.log(int(time.time())))
        # print(answer)

        textarea.send_keys(answer)
     
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()

        hidden_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        text = hidden_text.text

        if (text != "Correct!"):
            global msg
            msg += text
            print(msg)

        assert text == "Correct!", "Text is wrong" #check







