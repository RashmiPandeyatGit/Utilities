import os
import img2pdf

def imgtopdf(pdf,targetDirectory):
    with open(pdf, "wb") as f:
        f.write(img2pdf.convert(sorted([targetDirectory+i for i in os.listdir(targetDirectory) if i.endswith(".jpg")])))

targetDirectory = "image_source/"
pdf_name = "dummy.pdf"
imgtopdf(pdf_name,targetDirectory)
