from datetime import datetime


def convert_timestamp_in_str(timestamp):
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
    return str_date_time


# example:
timestamp = 1625309472.357246
print("Current timestamp", convert_timestamp_in_str(timestamp))
