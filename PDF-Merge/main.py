from PyPDF2 import PdfMerger

file1 = input("Enter the first file location: ")
file2 = input("Enter the second file location: ")
# array of PDFs which need to merge 
pdfs = [file1, file2]

merger = PdfMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged.pdf")
print('File Merger Complete.')
merger.close()
open("Merged_result.pdf")