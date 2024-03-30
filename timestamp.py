import config
import datetime

i = "information"
w = "warning"
e = "error"
f = "fail"


def timestamp():
    return datetime.datetime.now().strftime(config.timestamp)


def output(string, state):
    print(config.output % (state, timestamp(), string))
