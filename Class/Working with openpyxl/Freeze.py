# Program to freeze a column or row in spreadsheet using python

# Freeze is used to make sure that column or row headers are always visible as they scroll through the spreadhseet . They are called freeze panes
 
'''
Freeze Pane Settings          Rows and columns frozen

sheet.freeze_panes = 'A2'     Row 1
sheet.freeze_panes = 'B1'     Column A
sheet.freeze_panes = 'C1'     Columns A and B
sheet.freeze_panes = 'C2'     Row 1 and columns A and B
sheet.freeze_panes = 'A1'     No Fronzen Pane
sheet.freeze_panes = None     No Fronzen Pane

'''

import openpyxl

wb = openpyxl.load_workbook('Freeze.xlsx')

sheet = wb.active
# c = sheet['B2']
sheet.freeze_panes = 'B2'
wb.save('Freeze.xlsx')

