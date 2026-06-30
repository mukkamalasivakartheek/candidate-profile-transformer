import pycountry


def normalize_country(name):

    try:
        return pycountry.countries.lookup(name).alpha_2

    except:
        return None