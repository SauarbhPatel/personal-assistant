
# info imports and it's command
from datetime import datetime
import webbrowser
import pyttsx3  # ? pip install pyttsx3
import pywhatkit  # ? pip install pywhatkit
import speech_recognition as sr  # ? pip install SpeechRecognition
from sympy import content
import wikipedia
import os

# engine = pyttsx3.init('sapi5')
engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
voices = engine.getProperty('voices')
# print(voices)  # ? for print how many voices you have
# print(voices[2].id)  # ? how to set the particular voice
# engine.setProperty('voice', voices[2].id)
engine.setProperty('voice', voices[0].id)

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
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        # speak('Say that againn please....')
        return "None"

    return query


def sendEmail(to, content):
    pass


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'bob' in query:
            wishMe()
            speak('hii boss ..')
            while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                    speak('serching wikipedia')
                    query = query.replace('wikipedia', "")
                    results = wikipedia.summary(query, sentences=2)
                    speak('according to wikipedia')
                    speak(results)
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif 'play music' in query:
                    music_dir = 'C:\\Users\\saurabh patel\\Music\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                elif 'time batao' in query:
                    strTime = datetime.now().strftime("%H:%M:%S")
                    speak(f"boss, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\saurabh patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'email to harry' in query:
                    try:
                        speak('what should i say?')
                        content = takeCommand()
                        to = 'har@gmail.com'
                        sendEmail(to, content)
                        speak('Sended')
                    except Exception as e:
                        print(e)
                        speak("Sorry Boss. I am not able to send this email")
                        

                elif 'play' in query:
                    song = query.replace('play', '')
                    speak('playing' + song)
                    pywhatkit.playonyt(song)

                elif 'google search' in query:
                    speak('boss!, what do you want to search?')
                    content = takeCommand()
                    url = "https://www.google.com.tr/search?q={}".format(
                        content)
                    webbrowser.open(url)
                    
                elif 'whatsapp message' in query:
                    try:
                        speak('boss!, whom do you want to send message?')
                        name = takeCommand()
                        # info: finding the number
                        numbers = {'saurabh': 9669233736,'rahul': 1231231231}
                        for x, value in numbers.items():
                            if x==name:
                                number = value
                                break
                            else:
                                pass
                        hour = datetime.now().hour
                        minute = datetime.now().minute
                        second = datetime.now().second 
                        pywhatkit.sendwhatmsg(f"+91{number}", "Hello ", (hour),(minute+1 if second < 50 else minute+2), (10) , True, 5)
                        speak("Successfully Sent!")
                        
                    except:
                        # handling exception
                        print("An Unexpected Error!")

                # info : band karne ke liye
                elif 'band karo' in query:
                    print('bob is going to sleep')
                    break
                elif 'bob go to sleep' in query:
                    print('bob is going to sleep')
                    break

        else:
            print('bob is sleeping')
