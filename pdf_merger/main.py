# In this program i am going to write the code to merge two or more pdf's together.

'''
For this i am going to use the PyPDF2 library-: PyPDF2 is a free and open source pure-python PDF library
capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data,
viewing options, and passwords to PDF files. PyPDF2 can retrieve text and metadata from PDFs as well.
'''

import PyPDF2

pdffiles=["pdf1.pdf","pdf2.pdf","pdf3.pdf"]
# create an object for the pdfMerger class
merger=PyPDF2.PdfMerger()
# lopp through all the files in the pdffiles list.
for files in pdffiles:
    # open the files.
    pdf=open(files,"rb")
    #read the pdf using PdfReader()
    pdfreader=PyPDF2.PdfReader(pdf)
#     append the pdf's one by one in the merger object.
    merger.append(pdfreader)

# now finally write all the data in the new mergedpdffile.pdf
merger.write("Mergedpdfs.pdf")