from extractors.csv_extractor import extract_csv
from extractors.ats_extractor import extract_ats
from extractors.resume_extractor import extract_resume
from extractors.notes_extractor import extract_notes

from merge.merger import merge

from normalization.phones import normalize_phone
from normalization.skills import normalize_skill


def run_pipeline(paths):

    data = {}

    if paths.get("csv"):
        data["csv"] = extract_csv(paths["csv"])

    if paths.get("ats"):
        data["ats"] = extract_ats(paths["ats"])

    if paths.get("resume"):
        data["resume"] = extract_resume(
            paths["resume"]
        )

    if paths.get("notes"):
        data["notes"] = extract_notes(
            paths["notes"]
        )

    profile = merge(data)

    profile["candidate_id"] = "CAND-001"

    profile["phones"] = [
        normalize_phone(p)
        for p in profile.get("phones", [])
        if normalize_phone(p)
    ]

    profile["skills"] = [
        {
            "name": normalize_skill(s),
            "confidence": .9,
            "sources": ["resume"]
        }
        for s in profile.get("skills", [])
    ]

    return profile