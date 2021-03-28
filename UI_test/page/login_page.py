from time import sleep

from selenium.webdriver.common.by import By

from UI_test.page.base_page import BaseMethod


class Login(BaseMethod):
    def input_userinfo(self, username, password):
        self.find_sendkeys(By.ID, 'username', username)
        self.find_sendkeys(By.ID, 'password', password)
        self.action_click(By.XPATH, "/html/body/section/form/input[3]")
        sleep(2)

    def check_success(self):
        content = self.find(By.XPATH, '/html/body/h1').text()
        assert content == "登录成功"

