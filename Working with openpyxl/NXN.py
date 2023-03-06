import sys,openpyxl

if(len(sys.argv)!=2):
    n = 6
else:
    n = int(sys.argv[1])

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "NXN  multiplication"

for i in range(1,n+1):
    sheet.cell(row=1,column=i+1).value = i
    sheet.cell(row=i+1,column=1).value = i

for i in range(2,n+2):
    for j in range(2,n+2):
        sheet.cell(row=i,column=j).value = (i-1)*(j-1)

wb.save("multiplication.xlsx")