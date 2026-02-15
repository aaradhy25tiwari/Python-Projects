"""This is a python Program performing Text To Speech by Aaradhy"""
from tkinter.filedialog import askopenfilename
import pyttsx3 #import the pyttsx3 library
import pypdf

book = askopenfilename()
pdfreader = pypdf.PdfReader(book)

pages = len(pdfreader.pages)  # This tells us the total number of pages.

speaker = pyttsx3.init() #initialize the import

voices = speaker.getProperty('voices')       #getting details of current voice
speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

for num in range (pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

#This loop will go through every page starting from the given page number (8, here)
#and read the content of each page
