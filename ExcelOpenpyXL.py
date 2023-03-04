import openpyxl

wb = openpyxl.Workbook()
sheet =wb.active

sheet['A1'] = "G"

wb.save("Sameple.xlsx")