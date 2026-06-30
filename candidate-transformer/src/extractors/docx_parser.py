from docx import Document


def parse_docx(path: str) -> str:

    try:
        doc = Document(path)

        return "\n".join(
            para.text for para in doc.paragraphs
        )

    except Exception:
        return ""