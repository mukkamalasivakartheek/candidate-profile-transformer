import phonenumbers


def normalize_phone(phone):

    try:

        p = phonenumbers.parse(phone, "US")

        if phonenumbers.is_valid_number(p):
            return phonenumbers.format_number(
                p,
                phonenumbers.PhoneNumberFormat.E164
            )

    except:
        pass

    return None