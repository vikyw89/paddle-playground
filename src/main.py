from src.services.pdf_to_image import arun as arun_pdf
from src.services.any_to_pdfs import arun as arun_any
from src.services.pdf_to_markdowns import arun as arun_markdown
from src.services.image_to_text import arun as arun_image
import asyncio
from nest_asyncio import apply
apply()
# asyncio.run(arun_pdf())

asyncio.run(arun_image())


# asyncio.run(arun_any())
# asyncio.run(arun_markdown())