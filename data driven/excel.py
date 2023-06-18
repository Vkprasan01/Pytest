import Reader
print(Reader.get_row(path="C:/Users/lenovo/PycharmProjects/Seleniumproject/data driven/files/test.xlsx",sheetname="Sheet1"))
print(Reader.get_cell_data(path="C:/Users/lenovo/PycharmProjects/Seleniumproject/data driven/files/test.xlsx",sheetname="Sheet1",
                           row_number=1,column_number=2,data="prasanna"))