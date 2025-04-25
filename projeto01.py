import PyPDF2
import os

merger = PyPDF2.PdfMerger()
file_list = os.listdir('files')
file_list.sort()

for file in file_list:
    if file.endswith('.pdf'):
        merger.append(f'files/{file}')

merger.write('merged_output.pdf')
merger.close()

print("PDF merge completed successfully!")
