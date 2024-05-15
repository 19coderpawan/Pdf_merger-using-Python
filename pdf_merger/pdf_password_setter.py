# In this file i am going to write a program to set a password on a pdf.
import PyPDF2
pdffile="pdf2.pdf"
# create an object for the
# read the pdf using PdfReader.
pdfread=PyPDF2.PdfReader(pdffile)
# create an object for the Writer
pdfwriter=PyPDF2.PdfWriter()
# Add all pages in the pdfwriter
for pages in pdfread.pages:
    pdfwriter.add_page(pages)
# Encrypt it with password
pdfwriter.encrypt("pawan")
# Write it to an output file. (you can delete unencrypted version now)

# with open('encrypted_output.pdf', 'wb') as resultPdf:
#     pdfwriter.write(resultPdf)

# or
resultpdf=open("encrypted_output2.pdf","wb")
pdfwriter.write(resultpdf)
resultpdf.close()

# explanation
'''
. Import Library:

Python
import PyPDF2
Use code with caution.
content_copy
This line imports the PyPDF2 library, which provides functionalities for working with PDF files in Python. 
It's essential for reading, manipulating, and writing PDFs in this program.
2. Define PDF File Path:

Python
pdffile = "pdf1.pdf"
Use code with caution.
content_copy
This line assigns the file path of the PDF you want to password-protect to the variable pdffile. 
Make sure to replace "pdf1.pdf" with the actual path to your PDF file.
3. Create PDF Reader Object:

Python
pdfread = PyPDF2.PdfReader(pdffile)
Use code with caution.
content_copy
This line creates a PdfReader object from the PyPDF2 library. It opens the PDF file specified by pdffile 
in read mode, allowing you to access its content without modifying the original file.
4. Create PDF Writer Object:

Python
pdfwriter = PyPDF2.PdfWriter()
Use code with caution.
content_copy
This line creates a PdfWriter object from the PyPDF2 library. This object will be used to create a new 
PDF file with password protection.
5. Copy Pages:

Python
for pages in pdfread.pages:
    pdfwriter.add_page(pages)
Use code with caution.
content_copy
This loop iterates through all the pages (pages) in the original PDF (pdfread).
Inside the loop, the add_page(pages) method of pdfwriter adds each page from the original PDF to 
the new PDF being created. This essentially copies the content of the original document.
6. Encrypt PDF with Password:

Python
pdfwriter.encrypt("pawan")
Use code with caution.
content_copy
This line is the key part of password protection. It calls the encrypt() method of pdfwriter to set a 
password on the new PDF.
The argument "pawan" is the actual password you're setting. Choose a strong and secure password to 
effectively protect your PDF.
7. Write Encrypted PDF to Output File:

Python
with open('encrypted_output.pdf', 'wb') as resultPdf:
    pdfwriter.write(resultPdf)
Use code with caution.
content_copy
This line creates a new file named encrypted_output.pdf in write binary mode ('wb').
The with statement ensures proper file handling and automatic closing even if exceptions occur.
Inside the with block, the write() method of pdfwriter writes the encrypted PDF content 
(including the password protection) to the newly created output file.

'''