SOURCE_PRIORITY = {

    "resume": 4,
    "ats": 3,
    "csv": 2,
    "notes": 1
}


SOURCE_CONFIDENCE = {

    "resume": .90,
    "ats": .85,
    "csv": .80,
    "notes": .60
}


def choose_value(values):

    if not values:
        return None

    values = sorted(
        values,
        key=lambda x: SOURCE_PRIORITY[x["source"]],
        reverse=True
    )

    return values[0]


def merge(sources):

    profile = {}

    provenance = []

    all_fields = set()

    for source_name, source_data in sources.items():
        all_fields.update(source_data.keys())

    for field in all_fields:

        candidates = []

        for source_name, source_data in sources.items():

            if field in source_data and source_data[field]:

                candidates.append({
                    "value": source_data[field],
                    "source": source_name
                })

        winner = choose_value(candidates)

        if winner:

            profile[field] = winner["value"]

            provenance.append({
                "field": field,
                "source": winner["source"],
                "method": "priority_merge"
            })

    profile["provenance"] = provenance

    confs = []

    for p in provenance:
        confs.append(
            SOURCE_CONFIDENCE[p["source"]]
        )

    profile["overall_confidence"] = round(
        sum(confs) / len(confs),
        2
    ) if confs else 0

    return profile