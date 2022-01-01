import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_sticker_message(reply_token,package,sticker):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, StickerSendMessage(package_id=package, sticker_id=sticker))
    return "OK"

def send_button_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(  # 回復傳入的訊息文字
        reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='哈囉!媽咪\n想知道我最近在幹嘛嗎?',
                text='請選擇',
                actions=[
                    MessageTemplateAction(
                        label='三餐',
                        text='三餐'
                    ),
                    MessageTemplateAction(
                        label='生活',
                        text='生活'
                    ),
                    MessageTemplateAction(
                        label='課業',
                        text='課業'
                    ),
                    MessageTemplateAction(
                        label='花費',
                        text='花費'
                    )
                ]
            )
        )
    )
def push_button_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(  # 回復傳入的訊息文字
        reply_token,
        TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='哈囉!媽咪\n想知道我最近在幹嘛嗎?',
                text='請選擇',
                actions=[
                    MessageTemplateAction(
                        label='三餐',
                        text='三餐'
                    ),
                    MessageTemplateAction(
                        label='生活',
                        text='生活'
                    ),
                    MessageTemplateAction(
                        label='課業',
                        text='課業'
                    ),
                    MessageTemplateAction(
                        label='花費',
                        text='花費'
                    )
                ]
            )
        )
    )
def send_image_message(reply_token):
    image_message = ImageSendMessage(
        original_content_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2F9c8c1e647eb14e01898043c0c60bf03a&methods=resize%2C1000%2C5000',
        preview_image_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2Ffd2258c5ea6c43f591e8d9930d152b94&methods=resize%2C1000%2C5000'
    )
    line_bot_api = LineBotApi(channel_access_token,image_message)
    line_bot_api.reply_message(reply_token,)
#############################################################

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
