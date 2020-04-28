import inspect
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://form.jotform.com/200482139515350"
browser = webdriver.Chrome()

keyvalue = [
    {"#first_4" : "test"},
    {"#middle_4" : "dude"},
    {"#last_4" : "lastName"},
    {"#input_23_addr_line1" : "best street"},
    {"#input_23_addr_line2" : "second line"},
    {"#input_23_city" : "DC"},
    {"#input_23_state" : "Washington"},
    {"#input_23_postal" : "02346"},
    {"#input_6" : "Test@gmail.com"},
    {"#input_27_area" : "+370"},
    {"#input_27_phone" : "456798"},
    {"#input_14" : "Tile Based Solutions"},
    {"#input_45" : "last text input"},
]


browser.get(link)
for item in keyvalue:
    key = list(item.keys())[0]
    value = list(item.values())[0]
    browser.find_element_by_css_selector(key).send_keys(value)

dropdown = browser.find_element_by_css_selector('#input_3 > option:nth-child(2)')
dropdown.click();
time.sleep(3)
browser.find_element_by_css_selector('#input_20').click()




