import unittest

from selenium import webdriver

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


class someTesting(unittest.TestCase):
    def test_reg_1(self, link=link1):
        browser = webdriver.Chrome()
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
        self.assertEqual("Congratulations! You have successfully registered!", browser.find_element_by_tag_name('h1').text)
        browser.quit()

    def test_reg_2(self):
        self.test_reg_1(link2)


if __name__ == '__main__':
    unittest.main()
