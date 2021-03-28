from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethod:
    def __init__(self, driver: WebDriver=None):
        if driver is None:
            self.driver = webdriver.Chrome(executable_path='../driver/chromedriver')
            self.driver.get("http://127.0.0.1:5000/")
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def find(self, by, locator):
        element = self.driver.find_element(by, locator)
        return element

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def action_click(self, by, locator):
        action = ActionChains(self.driver)
        element = self.find(by, locator)
        print(element)
        action.click(element)
        action.perform()

    def find_sendkeys(self, by, locator, content):
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(content)

    def go_back(self):
        self.driver.back()




if __name__ == '__main__':
    a = BaseMethod()