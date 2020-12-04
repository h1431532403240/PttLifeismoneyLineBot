import datetime

def times(day):
    dayAgo = datetime.datetime.now() - datetime.timedelta(days = day)
    outPut = dayAgo.strftime("%m/%d")
    return outPut