from TestProject.Interface_test.dataconfig import data_config
from TestProject.Interface_test.util.Operation_excel import OperationExcel
from TestProject.Interface_test.util.Operation_json import OperationJson


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel("../data/interface_data.xlsx")
        self.opera_json = OperationJson("../data/login.json")

    # 获取用例条数
    def get_case_lines(self):
        nums = self.opera_excel.get_case_num()
        return nums

    # 获取用例是否执行
    def get_is_run(self, row):
        col = int(data_config.is_run())
        run = self.opera_excel.get_cell_vales(row, col)
        if run == "yes":
            return True
        else:
            return False

    # 获取用例是否有header
    def get_is_header(self, row):
        col = int(data_config.is_header())
        flag = self.opera_excel.get_cell_vales(row, col)
        return flag

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.request_method())
        request_method = self.opera_excel.get_cell_vales(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.request_url())
        request_url = self.opera_excel.get_cell_vales(row, col)
        return request_url

    # 获取依赖id
    def get_depend_id(self, row):
        col = int(data_config.depend_id())
        depend_id = self.opera_excel.get_cell_vales(row, col)
        return depend_id

    # 获取依赖的数据
    def get_depend_data(self, row):
        col = int(data_config.depend_data())
        depend_data = self.opera_excel.get_cell_vales(row, col)
        return depend_data

    # 获取依赖的字段
    def get_depend_field(self, row):
        col = int(data_config.depend_field())
        depend_filed = self.opera_excel.get_cell_vales(row, col)
        return depend_filed

    # 获取请求数据在json里的key
    def get_request_data_key(self, row):
        col = int(data_config.request_data())
        request_data = self.opera_excel.get_cell_vales(row, col)
        return request_data

    # 获取请求数据的json格式
    def get_request_data_json(self, row):
        key = self.get_request_data_key(row)
        request_data = self.opera_json.get_data(key)
        return request_data

    # 获取预期结果
    def get_expect_result(self, row):
        col = int(data_config.expect_result())
        expect_result = self.opera_excel.get_cell_vales(row, col)
        return expect_result


if __name__ == '__main__':
    data = GetData()
    print(data.get_request_data_json(2))



