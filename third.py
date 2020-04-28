from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

#browser.implicitly_wait(12)
WebDriverWait(browser, 10).until(
    expected_conditions.text_to_be_present_in_element(
        (By.ID, "price"),
        "$100"))

button = browser.find_element_by_id("book")
button.click()

x = browser.find_element_by_id("input_value")
y = str(math.log(abs(12 * math.sin(int(x.text)))))
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

time.sleep(30)
browser.quit();