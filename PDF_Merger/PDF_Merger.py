import PyPDF2, os

pdfFiles = []           
os.chdir("CURRENT WORKING DIRECTORY")

for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdfFiles.append(file)


pdfFiles.sort(key = str.lower)    
pdfWriter = PyPDF2.PdfWriter()      

for file in pdfFiles:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    for page in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        pdfWriter.add_page(pageObj)

resultPdf = open('Result.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()