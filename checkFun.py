# import speech_recognition as sr

# listener = sr.Recognizer()
# try:
#     with sr.Microphone() as source:
#         print('bolo')
#         voice = listener.listen(source,timeout=5, phrase_time_limit=5)
#         command = listener.recognize_google(voice)
#         print(command)
# except:
#     print('geting somme error')


# import speech_recognition as sr  # ? pip install SpeechRecognition
from datetime import datetime
# info: 0 to 24

# hour = int(datetime.now().hour)
# minute = datetime.now().minute
# second = datetime.now().second +45
# print(type(hour))  # info: 0 to 24
# print(type(minute))  # info: 0 to 24
# print(second)
# # listener = sr.Recognizer()
# l = sr.Recognizer()
# print('rec', sr.Recognizer())
# print('mic', sr.Microphone())
# with sr.Microphone() as source:
#     print('bolo')
#     voice = l.listen(source)
#     print('com')


# from rembg import remove
# from PIL import Image


# input_path = 'rbg.jpg'
# output_path = 'output.png'
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)

# import webbrowser

# url = "https://www.google.com.tr/search?q={}".format("Raspberry Pi")
# webbrowser.open(url)
# import pywhatkit
# Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+917987050249", "Hi", 12, 44)
# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

  # sending message to receiver
  # using pywhatkit
    name = 'saurabh'
    numbers = {'saurabh': 9669233736,'rahul': 1231231231}
    for x, value in numbers.items():
        if x==name:
            number = value
            break
        else:
            pass
    print(f"+91{number}")
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second 
    pywhatkit.sendwhatmsg(f"+91{number}", "Hello ", (hour),(minute+1 if second < 50 else minute+2), (10) , True, 5)
                          

except Exception as e:
    print(e)
