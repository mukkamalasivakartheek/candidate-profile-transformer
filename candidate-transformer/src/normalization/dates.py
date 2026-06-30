from dateutil import parser


def normalize_date(date_string):

    try:
        dt = parser.parse(date_string)

        return dt.strftime("%Y-%m")

    except:
        return None