import datetime


def time_to_second(h, m, s):
    result = datetime.timedelta(hours=h, minutes=m, seconds=s)
    result = result.total_seconds()
    return result


print(time_to_second(1, 0, 0))
print(time_to_second(0, 1, 0))
print(time_to_second(0, 0, 1))
