
# info imports and it's command
from datetime import datetime
import webbrowser
import pyttsx3  # ? pip install pyttsx3
import pywhatkit  # ? pip install pywhatkit
import speech_recognition as sr  # ? pip install SpeechRecognition
from sympy import content
import wikipedia
import os
from random import *
import webbrowser as web
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip 
from time import sleep
import wolframalpha # ? pip install wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)  # ? for print how many voices you have
# print(voices[2].id)  # ? how to set the particular voice
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# info : wishing 
def wishMe():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    elif hour >= 18 and hour > 22:
        speak('Good Evening!')

    else:
        speak('Good Night!')
# info : geting users details 
def getUserDetails():

    user = {'name': 'saurabh', 'gender': 'male'}
    return user;

# info: It takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  # ? stop for 1 sec
        r.energy_threshold = 10
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        query = query.lower()
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        # speak('Say that againn please....')
        return "None"

    return query


def sendWhatsAppMessage (number, message):
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second 
    pywhatkit.sendwhatmsg(f"+91{number}",  f"{message}", (hour),(minute+1 if second < 50 else minute+2), (10) , True, 5)

def videoDownloader():
    sleep(1)

    click(x=837,y=55)
    hotkey('ctrl','c')

    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('S:\\Private\\voiceAssistant\\Youtube Download Video\\')

    Download(Link)
    speak(' Download done.')
    os.startfile('S:\\Private\\voiceAssistant\\Youtube Download Video\\')

def saveURL():
    sleep(1)

    click(x=837,y=55)
    hotkey('ctrl','c')

    value = pyperclip.paste()
    Url = str(value)
    def saving(url):
        speak('what name should I save for this Url?')
        content = takeCommand()

        with open("allUrls.txt", "a") as file:
            file.write(
                f"{content} \t : {url} \n")
    saving(Url)

def saveSelectedText():
    # sleep(1)

    hotkey('ctrl','c')

    value = pyperclip.paste()
    Text = str(value)
    print(Text)
    def saving(text):
        speak('what name should I save for this text?')
        content = takeCommand()

        with open("allSelectedTexts.txt", "a") as file:
            file.write(
                f"{content} \t : {text} \n")
    saving(Text)

def FuntionIsRuning():
    user = getUserDetails()
    print(user['gender'])

    if user['gender'] == 'male':   
        speak('yes sir ..')
    else:
        speak('yes maam ..')

def wolfRam(query):
    apiKey = "WKVERQ-RRHV98EE23"
    requester = wolframalpha.Client(apiKey)
    requested = requester.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak('Sorry , i found some error')    

def Calculator(query):
    query.replace('multiply','*')
    query.replace('into','*')
    query.replace('add','+')
    query.replace('plus','+')
    query.replace('subtract','+')
    query.replace('minus','+')
    query.replace('divide','+')

    try:
        result = wolfRam(query)
        speak(f'Answer is, {result}')
    except:
        speak('Sorry , i found some error')


if __name__ == "__main__":
    while True:
        query = takeCommand()

        if 'bob' in query:
            user = getUserDetails()
            print(user['gender'])

            if ('bob good morning ' or 'bob good afternoon' or 'bob good evening' ) in query:
                wishMe()

            elif 'wake up'in query:
                if user['gender'] == 'male':
                    speak('ok sir ..')
                else:
                    speak('ok maam ..')

            elif 'hi 'in query:
                if user['gender'] == 'male':
                    speak('ok sir ..')
                else:
                    speak('ok maam ..')

            elif 'bob' in query:
                if user['gender'] == 'male':
                    speak('ok sir ..')
                else:
                    speak('ok maam ..')

                speak('How may i help you')



            while True:

                query = takeCommand()
                if 'bob' in query:

                    query = query.replace('bob', '')
                    
                    if 'wikipedia' in query:
                        FuntionIsRuning()
                        speak('serching wikipedia')
                        query = query.replace('wikipedia', "")
                        query = query.replace('according to', "")
                        results = wikipedia.summary(query, sentences=2)
                        speak('according to wikipedia')
                        speak(results)

                    elif 'open youtube' in query:
                        FuntionIsRuning()
                        webbrowser.open("youtube.com")

                    elif 'open facebook' in query:
                        FuntionIsRuning()
                        webbrowser.open("facebook.com")
                        
                    elif 'open whatsapp' in query:
                        FuntionIsRuning()
                        webbrowser.open("web.whatsapp.com")
                    

                    elif 'play music' in query:
                        FuntionIsRuning()
                        music_dir = 'C:\\Users\\saurabh patel\\Music\\Music'
                        songs = os.listdir(music_dir)
                        print(songs)
                        randomNumber =randint(0, len(songs)) 

                        os.startfile(os.path.join(music_dir, songs[randomNumber]))

                    elif 'time batao' in query:
                        FuntionIsRuning()
                        strTime = datetime.now().strftime("%H:%M:%S")
                        speak(f" the time is {strTime}")

                    elif 'save selected text' in query:
                        FuntionIsRuning()
                        saveSelectedText()
                        speak('done')

                    # info: calculator
                    elif 'calculator' in query:
                        FuntionIsRuning()
                        speak('what do you want to calculate')
                        query = takeCommand()
                        speak('wait for few seconds')

                        Calculator(query)
                        print('done')

                    # info: temperature
                    elif 'temperature' in query:
                        FuntionIsRuning()
                        # query = 'what is the temperature in rewa'
                        query.replace("what is the","")
                        query.replace("what","")
                        query.replace("is","")
                        query.replace("the","")
                        speak('wait for few seconds , i am searching')

                        temp = wolfRam(query)
                        print(temp)
                        speak(temp)

                    elif 'open code' in query:
                        FuntionIsRuning()
                        codePath = "C:\\Users\\saurabh patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)
                    
                    # info: open S drive
                    elif ('open s drive' or 'open yes drive') in query:
                        FuntionIsRuning()
                        codePath = "S:\\"
                        os.startfile(codePath)

                    # info: open C drive
                    elif 'open c drive' in query:
                        FuntionIsRuning()
                        codePath = "C:\\"
                        os.startfile(codePath)
                    # info: open C drive
                    elif 'open my private folder' in query:
                        FuntionIsRuning()
                        codePath = "S:\\Private\\"
                        os.startfile(codePath)

                    elif 'google search' in query:
                        speak(' what do you want to search?')
                        content = takeCommand()

                        url = "https://www.google.com.tr/search?q={}".format(
                            content)

                        webbrowser.open(url)

                    # info: if you want to search from youtube  
                    elif 'youtube search' in query:
                        speak('What do you want to search')
                        content = takeCommand()
                        result= 'https://www.youtube.com/results?search_query='+ content
                        web.open_new(result)


                    # info: to dowload a video from youtube  
                    elif 'download this video' in query:
                        FuntionIsRuning()

                        videoDownloader()

                    elif 'save this link' in query:
                        FuntionIsRuning()

                        print('link')
                        saveURL()

                    # info: play a song from youtube  
                    elif ('play a song' or ' listen a song') in query:
                        FuntionIsRuning()


                        if 'i want to' in query:
                            speak('What do you want to listen')
                            content = takeCommand()
                            pywhatkit.playonyt(content)

                        else:
                            pywhatkit.playonyt('new song')

                    elif 'whatsapp message' in query:

                        try:
                            speak(' whom do you want to send message?')
                            name = takeCommand()

                            # info: finding the number
                            numbers = {'saurabh': 9669233736,'rahul': 1231231231}

                            for x, value in numbers.items():
                                if x==name:
                                    number = value
                                    break

                                else:
                                    number = 'not found'

                            if number == 'not found':
                                speak("Sorry . I am not able to send this message")
                                speak(f'because this persion\'s data is not prasent ')
                                pass

                            else:
                                speak(f'what should i say to {name}?')
                                message = takeCommand()

                                sendWhatsAppMessage(number,message)

                                speak("Successfully Sent!")
                            
                        except Exception as e:

                            print(e)
                            speak("Sorry . I am not able to send this message")

                    # info : band karne ke liye
                    elif 'band karo' in query:
                        speak('ok  ..')

                        print('bob is going to sleep')
                        break

                    elif  'go to sleep' in query:
                        speak('ok  ..')

                        print('bob is going to sleep')
                        break


        elif 'stop the code' in query:
            speak('ok ..')
            break

        else:
            print('bob is sleeping')
