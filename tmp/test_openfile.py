import openpyxl


def test_use_excel():
    wb = openpyxl.load_workbook('../data/testcase.xlsx')
    # sh = wb.get_sheet_by_name('Sheet1')
    sh = wb.active
    data = list(sh.values)
    print(data)
    for line in data[1:]:
        print(line)


if __name__ == '__main__':
    test_use_excel()
