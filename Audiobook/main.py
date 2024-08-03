"""This is a python Program performing Text To Speech by Aaradhy"""
import pyttsx3 #import the pyttsx3 library
import pypdf

book = open('C:/Users/aarad/OneDrive/Desktop/Python/Python-Projects/Audiobook/Tutorial.pdf', 'rb')
#Here Tutorial.pdf should be replaced with the book or PDF you want to read.
# Also you need to add that file in the folder

pdfreader = pypdf.PdfReader(book)

pages = len(pdfreader.pages)  # This tells us the total number of pages.

speaker = pyttsx3.init() #initialize the import

voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#Here 8 is replaced by page number from which reading should start.
#Page index starts from 0, so 8 means page number 9
for num in range (8, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

#This loop will go through every page starting from the given page number (8, here)
#and read the content of each page
