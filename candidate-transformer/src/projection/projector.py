def get_nested(data, path):

    parts = path.replace("]", "").split("[")

    current = data

    for part in parts:

        if "." in part:

            for p in part.split("."):
                current = current.get(p)

        else:

            if part.isdigit():
                current = current[int(part)]
            else:
                current = current.get(part)

        if current is None:
            return None

    return current


def project(profile, config):

    result = {}

    for field in config["fields"]:

        out_name = field["path"]

        source_path = field.get(
            "from",
            field["path"]
        )

        value = get_nested(profile, source_path)

        if value is None:

            if config["on_missing"] == "omit":
                continue

            if config["on_missing"] == "error":
                raise Exception(
                    f"Missing {out_name}"
                )

        result[out_name] = value

    if config.get("include_confidence"):
        result["overall_confidence"] = \
            profile["overall_confidence"]

    return result