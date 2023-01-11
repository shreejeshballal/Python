# Program to manipulate the font styles of data that is present in a single cell

import openpyxl
from openpyxl.styles import Font 

# If we dont insert the above line then everytime we use Font function we have to use the entire statement openpyxl.styles.Font() instead of just Font()

wb = openpyxl.Workbook()
sheet =  wb.get_sheet_by_name('Sheet')

# Creating font objects
fontObj1 = Font(size=30,color="000000",bold=True,name='Times New Roman')  #keyword parameters
fontObj2 = Font(size=25,color="FF0000",name='Raleway',bold=True,italic=True)

# Inserting data into spreadsheet
sheet['A1'] = 'Hello World!'
sheet['A2'] = 'Python Presentation'
sheet['B1'] = 'Hello Class!'
sheet['B2'] = 'Mod5 Presentation'

# Assigning the font object to the desired cell 
sheet['A1'].font = fontObj1
sheet['A2'].font = fontObj2
sheet['B1'].font = fontObj1
sheet['B2'].font = fontObj2

# Resizing the col and row
sheet.row_dimensions[1].height = 100
sheet.row_dimensions[2].height = 100

sheet.column_dimensions['A'].width = 100
sheet.column_dimensions['B'].width = 100

# saving
wb.save('ColRowSize.xlsx')







