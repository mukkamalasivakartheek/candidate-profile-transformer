import re


def extract_notes(path):

    try:

        with open(path) as f:
            text = f.read()

        years = None

        m = re.search(r'(\d+)\+?\s+years', text)

        if m:
            years = int(m.group(1))

        return {
            "years_experience": years
        }

    except Exception:
        return {}