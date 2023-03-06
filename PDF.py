import PyPDF2
#first import then open the pdf file and save it. Then use the module along with PdfFileReader method to read the opened file. Once its done get the number of pages in pdf by using the object method called numPages and then get the page using getPage() method and later extract text from that page using extractText()
pdfObj = open('example.pdf')
pdfReader = PyPDF2.PdfFileReader(pdfObj)
print(pdfReader.numPages)
page = pdfReader.getPage(0)
text = page.extract_text()
print(text)


pdfEncbj = open('encrypted.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfEncbj)
if pdfReader.isEncrypted :
    print("This is an encrypted document")
    pdfReader.decrypt('rosebud')
    pdfPage = pdfReader.getPage(0)
else:
    pdfPage = pdfReader.getPage(0)



pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('explain.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for i in range(pdf1Reader.numPages):
    pdfpage = pdf1Reader.getPage(i)
    pdfWriter.addPage(pdfpage)
for i in range(pdf2Reader.numPages):
    pdfpage = pdf2Reader.getPage(i)
    pdfWriter.addPage(pdfpage)

pdf3Output = open("MergedFile","wb")
pdfWriter.encrypt("swordFish")
pdfWriter.write(pdf3Output)
pdf3Output.close()

