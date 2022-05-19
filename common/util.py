import datetime


def current_time():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d")
    # dt.strftime("%Y-%m-%d-%H-%M-%S")


# print(current_time())