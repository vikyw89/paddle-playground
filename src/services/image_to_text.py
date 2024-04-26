async def arun():
    from paddleocr import PaddleOCR

    ocr = PaddleOCR(lang="en")  # need to run only once to load model into memory
    import os

    current_dir = os.path.curdir
    input_dir = os.path.join(current_dir, "images")

    for file in os.listdir(input_dir):
        # check if it's a file
        if not os.path.isfile(os.path.join(input_dir, file)):
            continue
        img_path = os.path.join(input_dir, file)
        result = ocr.ocr(img_path, det=False, cls=False)
        output_file = os.path.join(current_dir, "texts", f"{file}.txt")

        with open(output_file, mode="a") as f:
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    print(line[0])
                    # f.write(line)
