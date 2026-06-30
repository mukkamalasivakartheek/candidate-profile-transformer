import json


def extract_ats(path):

    try:
        with open(path) as f:
            data = json.load(f)

        return {
            "full_name": data.get("candidateName"),
            "emails": [data.get("primaryEmail")]
            if data.get("primaryEmail") else [],
            "phones": [data.get("mobile")]
            if data.get("mobile") else [],
            "headline": data.get("jobTitle"),
            "location": {
                "city": data.get("city"),
                "region": data.get("state"),
                "country": data.get("country")
            },
            "skills": data.get("skills", [])
        }

    except Exception:
        return {}