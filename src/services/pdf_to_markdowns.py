async def arun():
    import pdf4llm
    import os

    current_dir = os.path.curdir
    input_dir = os.path.join(current_dir, "inputs")

    files = os.listdir(input_dir)

    for file in files:
        # check if it's a file
        file_path = os.path.join(input_dir, file)
        if not os.path.isfile(file_path):
            continue
        md_text = pdf4llm.to_markdown(os.path.join(input_dir, file))
        save_path = os.path.join(current_dir, "markdowns", f"{file.split('.')[0]}.md")
        with open(os.path.join(save_path), mode="w") as f:
            md_text = pdf4llm.to_markdown(file_path, pages=None)
            f.write(md_text)
