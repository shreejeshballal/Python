# Program to manipulate the font styles of data that is present in a single cell

import openpyxl
from openpyxl.styles import Font 

# If we dont insert the above line then everytime we use Font function we have to use the entire statement openpyxl.styles.Font() instead of just Font()

wb = openpyxl.Workbook()
sheet =  wb.get_sheet_by_name('Sheet')

# Creating font objects
fontObj1 = Font(size=30 , color="000000", bold=True ,name='Times New Roman')  #keyword parameters
fontObj2 = Font(size=25,color="FF0000",name='Raleway',bold=True)

# Inserting data into spreadsheet
sheet['A1'] = 'Hello World!'
sheet['A2'] = 'Python Presentation'

# Assigning the font object to the desired cell 
sheet['A1'].font = fontObj1
sheet['A2'].font = fontObj2

# Assinging the font object to the number of cells in the row or column
# for rowNum in range(1, 10):
#     sheet.cell(row=rowNum, column=2).font =fontObj1

wb.save('FontStyle.xlsx') 







