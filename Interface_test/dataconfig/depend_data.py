from TestProject.Interface_test.util.Operation_excel import OperationExcel


class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel_depend = OperationExcel("../data/interface_data.xlsx")

    # 根据 case_id 找到整行的数据
    def get_data_by_case_id(self,case_id):
        pass

    # 根据case_id找到行号
    def get_num_by_case_id(self, case_id):
        pass

    # 根据行号找到该行的内容
    def get_data_by_num(self, row):
        row_data = self.opera_excel_depend.get_row_value(row)
        return row_data


    # 获取某列的数据
    def get_cols_data(self, col_id=1):
        return self.opera_excel_depend.get_row_value()


