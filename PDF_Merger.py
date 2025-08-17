from PyPDF2 import PdfMerger
import sys

merger = PdfMerger()

param=0
amount_of_pdfs = len(sys.argv[1:])


while param<amount_of_pdfs:
    first_pdf = param
    pdf_file = sys.argv[first_pdf+1]
    merger.append(pdf_file)
    param+=1

output = open("merged_pdf.pdf","wb")
merger.write(output)
merger.close()
output.close()