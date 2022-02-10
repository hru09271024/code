from openpyxl import workbook , load_workbook

wd =  load_workbook('excel.xlsx')
ws = wd.active
print(ws)