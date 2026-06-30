import pandas as pd


def extract_csv(path):

    try:
        df = pd.read_csv(path)

        if df.empty:
            return {}

        row = df.iloc[0]

        return {
            "full_name": row.get("name"),
            "emails": [row.get("email")] if row.get("email") else [],
            "phones": [row.get("phone")] if row.get("phone") else [],
            "current_company": row.get("current_company"),
            "headline": row.get("title")
        }

    except Exception:
        return {}