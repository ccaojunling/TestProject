
class global_var:
    # 用例编号
    Id = '1'
    # 用例名称
    Name = '2'
    # 模块
    Model = '3'
    # 是否运行
    Run = '4'
    # 请求地址
    Url = '5'
    # 请求类型
    Method = '6'
    # 是否携带header
    Header = '7'
    # 被依赖的用例ID
    Depend_id = '8'
    # 被依赖的字段
    Depend_data = '9'
    # 哪个字段有依赖
    Depend_field = '10'
    # 请求数据在json里的key
    Request_data = '11'
    # 预期结果
    Respect_result = '12'


def case_id():
    return global_var.Id


def case_name():
    return global_var.Name


def model_name():
    return global_var.Model


def is_run():
    return global_var.Run


def request_url():
    return global_var.Url


def request_method():
    return global_var.Method


def is_header():
    return global_var.Header


def depend_id():
    return global_var.Depend_id


def depend_data():
    return global_var.Depend_data


def depend_field():
    return global_var.Depend_field


def request_data():
    return global_var.Request_data


def expect_result():
    return global_var.Respect_result


