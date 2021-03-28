# -*- coding:utf-8 -*-

from time import sleep
import pytest
import yaml
from UI_test.page.main_page import MainPage


# 解析数据文件
def get_data():
    with open('../datas/login_data.yml') as f:
        data = yaml.safe_load(f)
    user_info = data['login']
    return user_info


def get_name():
    with open('../datas/login_data.yml', encoding='UTF-8') as f:
        data = yaml.safe_load(f)
    name = data['name']
    print(name)
    return name


class TestLogin:

    def setup_class(self):
        print(1111111111111111111)
        self.main = MainPage()
        self.loginPage = self.main.goto_login()

    def teardown_class(self):
        print(222222222222)
        self.main.driver.quit()

    @pytest.mark.parametrize("userinfo", get_data(), ids=get_name())
    def test_login(self, userinfo):
        username = userinfo["username"]
        password = userinfo["password"]
        result = userinfo["result"]
        self.loginPage.input_userinfo(username, password)
        sleep(2)
        if result:
            self.main.go_back()