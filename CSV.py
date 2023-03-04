import csv
sample = open("Sample.csv")
sampleReader = csv.reader(sample)

for row in sampleReader:
    print('Row #'+str(sampleReader.line_num)+''+str(row))
    