# AudioBook - Turn your PDFs into Audio
## Requirements for this project are:
+ Python 3.10 and above
+ pyttsx3 library for text-to-speech functionality
+ PyPDF2 library for PDF parsing
    
## PyPDF Installation :
    pip install PyPDF2

## pyttsx3 Installation :

	pip install pyttsx3

> If you get installation errors , make sure you first upgrade your wheel version using :  
`pip install --upgrade wheel`
> Pyttsx3 library is dependent on win32 for which we may get an error while executing the program. To avoid that simply install pypiwin32 in your environment.
` pip install pypiwin32 `
> If you are using a virtual environment, make sure to install the library in the virtual environment.

## Usage :

```python3
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

**Single line usage with speak function with default options**

```python3
import pyttsx3
pyttsx3.speak("I will speak this text")
```
	
**Changing Voice , Rate and Volume :**

```python3
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

```

### **Full documentation of the Library**

https://pyttsx3.readthedocs.io/en/latest/
