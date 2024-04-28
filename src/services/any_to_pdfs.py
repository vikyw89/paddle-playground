import os
import fitz

async def arun():
    current_dir = os.path.curdir
    input_dir = os.path.join(current_dir, "any")

    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        raw_file = fitz.open(file_path)
        pdf_file = raw_file.convert_to_pdf()

        with open(os.path.join(current_dir, "pdfs", f"{file.split('.')[0]}.pdf"), mode="wb") as f:
            f.write(pdf_file)
        