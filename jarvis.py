
# Install this packages
# pip install SpeechRecognition pyttsx3 wikipedia pywhatkit pyaudio

# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (0 for male)
engine.setProperty('rate', 150)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I assist you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print("Sorry, I didn’t catch that.")
        return "https://google.com"
    return command.lower()

def run_jarvis():
    wish_user()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Let me search that on Google.")
            pywhatkit.search(query)

run_jarvis()