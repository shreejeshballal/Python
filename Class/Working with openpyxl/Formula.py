# Program to usage of formula in sheet using python

import openpyxl

# Loading workbook into a variable
wb = openpyxl.load_workbook('Formula.xlsx')
sheet = wb.active

# Finding sum and average
sheet['G17'] = '=sum(G14:G16)'
sheet['G18'] = '=average(G14:G16)'


wb.save('Formula.xlsx')


