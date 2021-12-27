'''
Project: Combining Select Pages from Many PDFs
Say you have the boring job of merging several dozen PDF documents into a single PDF file. 
Each of them has a cover sheet as the first page, 
but you don’t want the cover sheet repeated in the final result. 
Even though there are lots of free programs for combining PDFs, 
many of them simply merge entire files together. 
Let’s write a Python program to customize which pages you want in the combined PDF.
'''  
   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # into a single PDF.
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
# TODO: Loop through all the pages (except the first) and add them.
    for pagenum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pagenum)
        pdfWriter.addPage(pageObj)
# TODO: Save the resulting PDF to a file.
outputfile = open('new.pdf', 'wb')
pdfWriter.write(outputfile)
outputfile.close()