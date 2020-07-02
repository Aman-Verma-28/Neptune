import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import os
import sys
import wikipedia
import wolframalpha
import pyaudio 
import subprocess
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("Voice",voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("Processing....")
        query=r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception:
        print("Could not process the input")
        print("Say that again please")
        speak("Could not process the input")
        speak("Say that again please")
        speak("Try typing the command: ")
        query=input("Enter your command here: ")
    return query



if __name__ == "__main__":
    print("Neptune said: Hello! My name is Neptune, I am a voice Assistant.")
    speak("Hello! My name is Nep tune, I am a voice Assistant.")
    print("Neptune said: How may I help you?")
    speak("How may I help you?")
    while True:
        query=command().lower()
        if "who are" in query:
            print("Neptune said: I am created by Aman and I live in your computer!! ")
            speak("I am created by Aman and. I live in your computer!!")
            print("Neptune said: My job is to make your life easy")
            speak("My job is to make your life easy")
        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            speak("Acording to wikipedia")
            print("Neptune said: ",result)
            speak(result)
            

        elif "open youtube" in query:
            speak("okay . Opening")
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("okay  . Opening")
            webbrowser.open("www.google.com")
        elif "open mail" in query:
            speak("okay  . Opening")
            webbrowser.open("www.gmail.com")
        elif "open music" in query:
            speak("okay  . Opening")
            subprocess.call("C:\\Users\\verma\\AppData\\Roaming\\Microsoft\\Windows\\\Start Menu\\Programs\\Spotify.exe")
        elif "open hacker" in query:
            speak("okay  . Opening")
            webbrowser.open("www.hackerrank.com")
        elif "open stacks" in query:
            speak("okay  . Opening")
            webbrowser.open("www.stacksoverflow.com")
            
        elif "exit" in query:
            print("Thank you sir for your time.Bye")
            speak("Thank you sir for your time.  Bye")
            sys.exit()
        elif "open notepad" in query:
            speak("okay  . Opening")
            subprocess.call("notepad.exe")
        elif "open calculator" in query:
            speak("okay  . Opening")
            subprocess.call("calculator.exe")