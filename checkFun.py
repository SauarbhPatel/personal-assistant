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
# # from datetime import datetime
# # print(datetime.now().hour)  # info: 0 to 24


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
import pywhatkit
# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+919669233736", "Hi", 11, 7,15, True, 60)