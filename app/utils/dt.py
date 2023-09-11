import datetime


def parse_datetime(datetime_string, tz=datetime.timezone.utc):
    # Thu Dec 01 15:28:40 +0000 2022
    return datetime.datetime.strptime(
        datetime_string, '%a %b %d %H:%M:%S %z %Y'
    ).replace(tzinfo=tz)
