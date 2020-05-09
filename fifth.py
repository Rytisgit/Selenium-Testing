import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLoginForm:
    def test_should_login_if_correct_form(self, browser, link=link1):
        browser.get(link)
        browser.implicitly_wait(1)

        browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("name")
        browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("lastname")
        browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("name")

        button = browser.find_element_by_css_selector("body > div > form > button")
        button.click()
        assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"

    def test_should_throw_exception_if_different_form(self, browser):
        with pytest.raises(NoSuchElementException):
            self.test_should_login_if_correct_form(browser, link2)
