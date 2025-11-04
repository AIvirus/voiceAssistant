import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'partner' in command:
                command = command.replace('partner', '')
                print(command)
    except:
        pass
    return command

def run_partner():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who is your creator' in command:
        talk('I was created by a Praveen to assist and communicate effectively. They did a great job, don’t you think?')
    elif 'what can you do' in command:
        talk('I can perform a variety of tasks like searching for information, answering questions, and helping you stay productive. What would you like me to do first?')
    elif 'who are you' in command:
        talk('I am your virtual assistant, designed to make your work easier and more efficient. How can I assist you today?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_partner()
