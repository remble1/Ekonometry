from openpyxl import load_workbook

wb2 = load_workbook('dane.xlsx')
print(wb2.sheetnames)


