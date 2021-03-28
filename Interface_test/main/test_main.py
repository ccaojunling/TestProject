import json

import pytest

from TestProject.Interface_test.base.runmethod import RunMethod
from TestProject.Interface_test.dataconfig.get_data import GetData


class Testhttp:
    def __init__(self):
        self.main = RunMethod()
        self.data = GetData()

    def verify_result(self, str_one, str_two):
        if str(str_one) in str(str_two):
            return True
        else:
            return False

    # 运行用例
    def go_on_run(self):
        result = []
        row_count = self.data.get_case_lines()
        print(row_count)
        for i in range(2, row_count+1):
            is_run = self.data.get_is_run(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            expect_result = self.data.get_expect_result(i)
            if method == 'post':
                data = self.data.get_request_data_json(i)
            else:
                data = None
            if is_run:
                res = self.main.run_main(method=method, url=url, data=data)
                # print(res.status_code)
                response_data = json.loads(res.text)
                # print(json.dumps(json.loads(res.text), indent=2))

                if self.verify_result(expect_result, response_data):
                    print("测试通过")
                else:
                    print("测试失败")


if __name__ == '__main__':
    a = Testhttp()
    a.go_on_run()

