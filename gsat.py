from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
import time
import datetime
#今天日期 (2006-11-18)
today = datetime.date.today()
#設定要相減的日期
other_day = datetime.date(2021,1,22)
result = other_day - today
CHANNEL_ACCESS_TOKEN = ""
to = ""
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

#文字訊息

try:
    line_bot_api.push_message(to, TextSendMessage("再 " + str(result.days) + " 天就要學測了"))
except LineBotApiError as e:
    # error handle
    raise e

