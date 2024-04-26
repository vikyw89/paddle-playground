from src.services.pdf_to_image import arun as arun_pdf
from src.services.image_to_text import arun as arun_image
from src.services.pdf_to_markdowns import arun as arun_markdown
import asyncio

# asyncio.run(arun_pdf())

# asyncio.run(arun_image())

asyncio.run(arun_markdown())