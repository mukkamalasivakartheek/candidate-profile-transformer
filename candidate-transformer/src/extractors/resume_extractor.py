from pathlib import Path

from .pdf_parser import parse_pdf
from .docx_parser import parse_docx
from .text_extraction import extract_fields


def extract_resume(path: str):

    ext = Path(path).suffix.lower()

    if ext == ".pdf":
        text = parse_pdf(path)

    elif ext == ".docx":
        text = parse_docx(path)

    else:
        return {}

    return extract_fields(text)