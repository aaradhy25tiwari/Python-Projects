import datetime
import smtplib
import webbrowser
from tkinter import *

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition

root = Tk()
root.geometry("655x335")
root.title("Announcement")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
 
def announce():
    wishMe()
    speak("Attention Ladies and Gentlemen, Train number") 
    speak((trainnovalue).get())
    speak(trainnamevalue.get())
    speak("arriving from")
    speak(fromlocvalue.get())
    speak("and going to")
    speak(tolocvalue.get())
    speak("via")
    speak(viavalue.get())
    speak("is arriving on plateform number")
    speak(platformvalue.get())

Label(root, text="Form Title", font="comicsans 13 bold", pady=10).grid(row=0, column=0)

trainno = Label(root, text="Train No.")
trainname = Label(root, text="Train Name")
fromloc = Label(root, text="Arriving from")
toloc = Label(root, text="Going to")
via = Label(root, text="Via")
platform = Label(root, text="Platform No.")

trainno.grid(row=1, column=0)
trainname.grid(row=2, column=0)
fromloc.grid(row=3, column=0)
toloc.grid(row=4, column=0)
via.grid(row=5, column=0)
platform.grid(row=6, column=0)

trainnovalue = StringVar()
trainnamevalue = StringVar()
fromlocvalue = StringVar()
tolocvalue = StringVar()
viavalue = StringVar()
platformvalue = StringVar()

trainnoentry = Entry(root, textvariable=trainnovalue)
trainnameentry = Entry(root, textvariable=trainnamevalue)
fromlocentry = Entry(root, textvariable=fromlocvalue)
tolocentry = Entry(root, textvariable=tolocvalue)
viaentry = Entry(root, textvariable=viavalue)
platformentry = Entry(root, textvariable=platformvalue)

trainnoentry.grid(row=1,column=3)
trainnameentry.grid(row=2,column=3)
fromlocentry.grid(row=3,column=3)
tolocentry.grid(row=4,column=3)
viaentry.grid(row=5,column=3)
platformentry.grid(row=6,column=3)

Button(text="SUBMIT", command=announce).grid(row=7, column=3)

root.mainloop()