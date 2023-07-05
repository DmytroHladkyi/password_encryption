from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdfwriter = PdfWriter()
pdf = PdfReader(r'C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\project10_password _encryption\InTime.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password= getpass(prompt="Podaj hasło: ")
pdfwriter.encrypt(password)

with open(r'C:\Users\Hladkyi Dmytro\Desktop\IT Oprogromowanie\Python_Projects\project10_password _encryption\InTime11.pdf', 'wb') as file:
    pdfwriter.write(file)

    pdfwriter.add_page(pdf.pages[page])
