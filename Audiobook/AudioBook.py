"""This is a python Program performing Text To Speech by Aaradhy"""
import pyttsx3 #import the pyttsx3 library

speaker = pyttsx3.init() #initialize the import
speaker.say("Hello I am Audios, your reading patner")
speaker.runAndWait()
