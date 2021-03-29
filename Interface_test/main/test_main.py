import json

import pytest

from TestProject.Interface_test.base.runmethod import RunMethod
from TestProject.Interface_test.dataconfig.data_config import request_method, request_url, request_data
from TestProject.Interface_test.dataconfig.depend_data import DependData
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
            is_depend = self.data.get_depend_id(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            expect_result = self.data.get_expect_result(i)
            if method == 'post':
                data = self.data.get_request_data_json(i)
            else:
                data = None
            if is_run:
                # 判断没有依赖的时候
                if is_depend is None:
                    res = self.main.run_main(method=method, url=url, data=data)
                    # print(res.status_code)
                    response_data = json.loads(res.text)
                    # print(json.dumps(json.loads(res.text), indent=2))
                    if self.verify_result(expect_result, response_data):
                        print("测试通过")
                    else:
                        print("测试失败")
                else:
                    depend_data = list(DependData(is_depend).get_data_by_case_id())
                    print(depend_data)
                    request_method_id = int(request_method())
                    url_id = int(request_url())
                    data_id = int(request_data())
                    if depend_data[request_method_id] == 'post':
                        depend_request_data = self.data.get_request_data_json(depend_data[data_id-1])
                    else:
                        depend_request_data = None
                    # res = self.main.run_main(method=depend_data[request_method_id], url=depend_data[url_id], data=depend_request_data)
                    print(depend_data[request_method_id-1], depend_data[url_id-1], depend_request_data)





if __name__ == '__main__':
    a = Testhttp()
    a.go_on_run()

