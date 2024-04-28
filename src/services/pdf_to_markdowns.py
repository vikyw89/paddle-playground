async def arun():
    import pdf4llm
    import os
    import fitz
    current_dir = os.path.curdir
    input_dir = os.path.join(current_dir, "pdfs")

    files = os.listdir(input_dir)

    for file in files:
        # check if it's a file
        file_path = os.path.join(input_dir, file)
        if not os.path.isfile(file_path):
            continue
        save_path = os.path.join(current_dir, "markdowns", f"{file.split('.')[0]}.md")
        with open(save_path, mode="w") as f:
            md_text = pdf4llm.to_markdown(doc=file_path)
            f.write(md_text)
