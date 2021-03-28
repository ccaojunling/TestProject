from selenium.webdriver.common.by import By

from UI_test.page.base_page import BaseMethod
from UI_test.page.login_page import Login
from UI_test.page.register_page import Register


class MainPage(BaseMethod):
    def goto_login(self):
        self.find_and_click(By.ID, 'btn1')
        return Login(self.driver)

    def goto_register(self):
        self.find_and_click(By.ID, 'btn2')
        return Register(self.driver)
