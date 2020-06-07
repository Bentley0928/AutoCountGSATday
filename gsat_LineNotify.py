import requests
import time
import datetime
#今天日期 (2006-11-18)
today = datetime.date.today()
#設定要相減的日期
other_day = datetime.date(2021,1,22)
result = other_day - today
weekend = int((result.days)/7)
# TextSendMessage("再 " + str(result.days) + " 天就要學測了, " + "還有 " + str(weekend) + " 個週六日"))

Message = "再 " + str(result.days) + " 天就要學測了, " + "還有 " + str(weekend) + " 個週六日"
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

msg = Message
token = ''

lineNotifyMessage(token, msg)
