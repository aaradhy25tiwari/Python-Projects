"""Language translator application using Deep Translator."""
from tkinter import Tk, Text, Frame, Button, END, GROOVE, WORD
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

window = Tk()
window.title("DataFlair Language Translator")
window.minsize(600,500)
window.maxsize(600,500)

def translate():
    """Translate text from source to target language."""
    global language
    try:
        txt = text1.get(1.0, END).strip()
        c2 = combo2.get()
        if txt:
            lan_ = language.get(c2)
            if lan_ is None:
                messagebox.showerror("Error", "Selected language not found")
                return
            translator = GoogleTranslator(source='auto', target=lan_)
            result = translator.translate(txt)
            text2.delete(1.0, END)
            text2.insert(END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")



language = GoogleTranslator().get_supported_languages(as_dict=True)
lang_value = list(language.keys())

combo1=ttk.Combobox(window,values=lang_value,state='r')
combo1.place(x=100,y=20)
combo1.set("choose a language")



f1=Frame(window,bg='black',bd=4)
f1.place(x=100,y=100,width=150,height=150)

text1=Text(f1,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=140,height=140)

combo2=ttk.Combobox(window,values=lang_value,state='r')
combo2.place(x=300,y=20)
combo2.set("choose a language")

f2=Frame(window,bg='black',bd=4)
f2.place(x=300,y=100,width=150,height=150)

text2=Text(f2,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=140,height=140)

button = Button(window,text='Translate',font=('normal',15), bg='yellow', command=translate)
button.place(x=230,y=300)# button which when triggered performs translation


window.mainloop()
