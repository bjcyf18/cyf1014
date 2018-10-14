#coding:utf-8
import  xlrd
import sys
import os
sys.path.append("..")
from config import config as cf
#从excel中获取一行用例的数据
#data_file:数据文件，sheet 所在表明 case_name 用例名称
def get_case_data(data_file,sheet,case_name):
    data_file_path=os.path.join(cf.data_path,data_file) #找到文件
    wb=xlrd.open_workbook(data_file_path) #打开excel
    sh=wb.sheet_by_name(sheet) #找到工作表
    for i in range(1,sh.nrows):
        if sh.cell(i,0).value==case_name:
            return sh.row_values(i)



# excel=xlrd.open_workbook("data.xlsx")
# sheet=excel.sheet_by_name("TestUserLogin")
# print(sheet.cell(0,0).value) #0行0列
# print(sheet.cell(1,2).value) #1行1列

# print(sheet.nrows)
# print(sheet.ncols)

#打印excel所有单元格的数据

# for i in range(1,sheet.nrows):
#     for j in range(0,sheet.ncols):
#         print(sheet.cell(i,j).value)
#
# print(sheet.row_values(1))

#输出所有行的数据
# for i in range(1,sheet.nrows):
#     print(sheet.row_values(i))
# for i in range(1,sheet.nrows):
#     if sheet.cell(i,0).value=='test_01':
#        print(sheet.row_values(i))
#返回excel sheet的所有数据

# def excel_to_list(data,sheet_name):
#     excel=xlrd.open_workbook(data)
#     sheet=excel.sheet_by_name("TestUserLogin")
#     result=[]
#     for i in range(1, sheet.nrows):
#         result.append(sheet.row_values(i))
#         print("添加成功")
# #
#     return result
# def get_test_data(data_list,case_name):
#     for case_data in data_list:
#         if case_data[0]==case_name:
#             return case_data

# def get_data(file,sheet_name,casename):
#     wb=xlrd.open_workbook(file)
#     sh=wb.sheet_by_name(sheet_name)
#
#     for i in range(1,sh.nrows):
#         if sh.cell(i,0).value==casename:
#             return sh.row_values(i)
#
#
if __name__=='__main__':
    # print(excel_to_list('data.xlsx',"TestUserLogin"))
    #   data_list=excel_to_list('data.xlsx','TestUserLogin')
    #   print(get_test_data(data_list,'test_01'))
    case_data=get_case_data('data.xlsx','TestUserLogin','test_01')
    print(case_data)
    url=case_data[1]
    data=case_data[3]
    expect_res=case_data[4]
    print(url)
    print(data)
    print(expect_res)

