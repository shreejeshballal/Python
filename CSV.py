import csv
sample = open("Sample.csv")
sampleReader = csv.reader(sample)

sampleData = list(sampleReader)
print(sampleData)

print(sampleData[0][0])

for row in sampleReader:
    print('Row #'+str(sampleReader.line_number)+" "+str(row))

sampleW = open("Sample.csv","w")
sampleWriter = csv.writer(sampleW)
sampleWriter.writerow(['row', 'sample', 'sampleData'])
sampleWriter.writerow(['row', 'sample', 'sampleData'])
sampleWriter.writerow(['row', 'sample', 'sampleData'])
sampleW.close()