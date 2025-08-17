import os
from typing import List

from PyPDF2 import PdfReader,PdfWriter
import sys



content_pdf= sys.argv[1]
stamp_pdf= sys.argv[2]
pdf_result= None
page_indices = "ALL"

if len(sys.argv) >= 4:
    pdf_result = sys.argv[3]
else:
    base, ext = os.path.splitext(sys.argv[1])
    pdf_result = base + "_watermarked" + ext

reader = PdfReader(content_pdf)
if page_indices == "ALL":
    page_indices = list(range(0, len(reader.pages)))

writer = PdfWriter()
for index in page_indices:
    content_page = reader.pages[index]
    mediabox = content_page.mediabox

    # You need to load it again, as the last time it was overwritten
    reader_stamp = PdfReader(stamp_pdf)
    image_page = reader_stamp.pages[0]

    image_page.merge_page(content_page)
    image_page.mediabox = mediabox
    writer.add_page(image_page)

output = open(pdf_result, "wb")
writer.write(output)
output.close()