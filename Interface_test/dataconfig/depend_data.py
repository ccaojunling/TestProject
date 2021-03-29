from TestProject.Interface_test.util.Operation_excel import OperationExcel


class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel_depend = OperationExcel("../data/interface_data.xlsx")

    # 根据 case_id 找到整行的数据
    def get_data_by_case_id(self):
        row = self.get_num_by_case_id()
        return self.get_data_by_num(row)

    # 根据case_id找到行号
    def get_num_by_case_id(self):
        col_data = self.get_cols_data()
        return col_data.index(self.case_id)+1

    # 根据行号找到该行的内容
    def get_data_by_num(self, row):
        row_data = self.opera_excel_depend.get_row_value(row)
        return row_data

    # 获取某列的数据,col_id 是列号A，B，C等，默认第一列
    def get_cols_data(self, col_id='A'):
        col_data = self.opera_excel_depend.get_col_value(col_id)
        return col_data

1
if __name__ == '__main__':
    dd = DependData(1)
    print(dd.get_data_by_case_id())
