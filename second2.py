from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

browser.get(link)

button = browser.find_element_by_css_selector("body > form > div > div > button")
button.click()

browser.switch_to.window(browser.window_handles[1])

x = browser.find_element_by_id("input_value");
y = str(math.log(abs(12 * math.sin(int(x.text)))));
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

button = browser.find_element_by_css_selector("body > form > div > div > button")
button.click()

time.sleep(30)
browser.quit();