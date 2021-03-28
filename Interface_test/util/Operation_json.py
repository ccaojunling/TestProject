import json


class OperationJson:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.filename, encoding='utf-8') as f:
            data = json.load(f)
            return data

    # 根据关键字获取数据
    def get_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    op = OperationJson("../data/login.json")
    print(op.read_data())
    print(op.get_data("login"))