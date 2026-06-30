import pdfplumber


def parse_pdf(path: str) -> str:
    text = ""

    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception:
        return ""

    return text