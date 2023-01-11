import openpyxl
from openpyxl.chart import Reference, LineChart

wb = openpyxl.load_workbook('Chart.xlsx')
sheet = wb.active

# Data for plotting
# Choose all the data from Column 2 to 4
values = Reference(sheet,min_col=2,max_col=4,min_row=1,max_row=11)

# Create object of LineChart class
chart = LineChart()

chart.add_data(values, titles_from_data=True)


# set the title of the chart
chart.title = "Analysis Stock prices"

# set the title of the x-axis
chart.x_axis.title = "Date"

# set the title of the y-axis
chart.y_axis.title = "Stock Value"

# the top-left corner of the chart is anchored to cell F2 .
sheet.add_chart(chart,"F2")

# save the file 
wb.save("Chart.xlsx")