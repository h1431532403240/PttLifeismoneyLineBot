import datetime

# 輸入整數取得日期，如今日為12/12，輸入-1則會回傳12/11
def times(day):
    dayAgo = datetime.datetime.now() + datetime.timedelta(days = day)
    outPut = dayAgo.strftime("%m/%d")
    return outPut