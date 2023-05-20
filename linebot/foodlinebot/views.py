from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

#line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
line_bot_api = LineBotApi('2YnfFy6Rf+qkkuWedKQHRfJ21Qh/Ztvp6Mx3BXz26tcEwvIQ4QAxrIoHS5Shno37Gpr0d021ZiYMVP7z2FMdRgzE+VKAluhCPA1mchUnBLnAnjAkzS9kkFxGI02rjQECninRwLJ74nJN+lbuAM9+7wdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('fd992488416e202095dfa8d28d053992')

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()