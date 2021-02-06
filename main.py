import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("I am your Alexa. Please tell me how may I help you")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            engine.runAndWait()
            #listener.energy_threshold = 4000
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print('Boss :', command)
    except:
        print("Say that again...")
        return "None"
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'search' in command:
        talk('Searching Wikipedia...')
        command = command.replace('search', '')
        info = wikipedia.summary(command, 2)
        print(info)
        talk('According to wikipedia...')
        talk(info)
    #elif 'date' in command:
        #talk('sorry boss, I am not interested')
    elif 'are you single' in command:
        talk('Sorry boss, i am in a relationship with wifi')
    elif 'joke' in command:
        j = pyjokes.get_joke()
        print(j)
        talk("Here's the joke...")
        talk(j)
    elif 'open google' in command:
        talk('Opening google...')
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        talk('Opening stack overflow...')
        webbrowser.open("stackoverflow.com")
    elif 'open github' in command:
        talk('Opening Git Hub...')
        webbrowser.open("github.com//eshadas")
    elif 'open code' in command:
        talk('Opening microsoft VS code...')
        code = "C:\\Users\\souvik das\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code)
    elif 'off' in command:
        talk('good bye boss, May all of your efforts yield a positive outcome......see you soon')
        exit()
    else:
        talk('Please say the command again.')
wishMe()
while True:
    run_alexa()
