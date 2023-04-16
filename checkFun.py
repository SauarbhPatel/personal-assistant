# -*- coding: utf-8 -*-
from translate import Translator
from time import sleep
import pywhatkit  # ? pip install pywhatkit
from datetime import datetime
# import os
# def get_user():
#     return os.getenv('USER',os.getenv('USERNAME','none' ))

# print(get_user())


def sendWhatsAppMessage(number, message):
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    pywhatkit.sendwhatmsg(f"+91{number}",  f"{message}", (hour),
                          (minute+1 if second < 50 else minute+2), (10), True, 5)


# sendWhatsAppMessage('8349895717', 'hello zafarn khan')
translator = Translator(to_lang="Hindi")
translation = translator.translate("Good Morning!")
print(translation)
