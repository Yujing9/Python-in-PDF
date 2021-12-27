#Cut out specific pages from PDFs.
import PyPDF2, os
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
# TODO: Loop through all the PDF files.
for files in pdfFiles:
    file = open(files, 'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    pageObj = pdfReader.getPage(3)
    pdfWriter.addPage(pageObj)
# TODO: Save the resulting PDF to a file.
outputfile = open('new.pdf', 'wb')
pdfWriter.write(outputfile)
outputfile.close()
