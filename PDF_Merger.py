from PyPDF2 import PdfFileWriter
import sys
merger = PdfFileWriter()
param=0
for param in sys.argv:
    pdf = sys.argv[param+1]
    merger.appendPagesFromReader(pdf)

merger.write("merged_pdf.pdf")
merger.close()

"""
with open("dummy.pdf","rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf","wb") as file2:
        writer.write(file2)
        """