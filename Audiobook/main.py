"""This is a python Program performing Text To Speech by Aaradhy"""
import pyttsx3 #import the pyttsx3 library
import PyPDF2

book = open('Tutorial.pdf', 'rb') 
# Here Tutorial.pdf should be replaced with the book or PDF you want to read. Also you need to add that file in the folder

pdfreader = PyPDF2.PdfFileReader(book)

pages = pdfreader.numPages # This tells us the total number of pages.

speaker = pyttsx3.init() #initialize the import

#Here 8 is replaced by page number from which reading should start. Page index starts from 0, so 8 means page number 9
for num in range (8, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

#This loop will go through every page starting from the given page number (8, here) and read the content of each page
