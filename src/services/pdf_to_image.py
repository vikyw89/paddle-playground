async def arun():
    import fitz  # import the bindings
    import os

    current_dir = os.path.curdir
    input_dir = os.path.join(current_dir, "inputs")

    files = os.listdir(input_dir)

    for f in files:
        fname = os.path.join(input_dir, f)
        # check if it's a file
        if not os.path.isfile(fname):
            continue

        print(fname)
        doc = fitz.open(fname)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap()  # render page to an image

            # generate a save path
            save_path = os.path.join(
                current_dir, "images", f"{f.split('.')[0]}-{page.number}.png"
            )
            # pix.save("page-%i.png" % page.number)  # store image as a PNG
            pix.save(save_path)
