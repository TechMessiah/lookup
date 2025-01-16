import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from gtts import gTTS
import pygame
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import requests

pygame.mixer.init()

def lookUp(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    results = response.json()

    result = dict({
        "phonetics": results[0]["phonetics"],
        "meanings": results[0]["meanings"],
    })
    
    return result

# function used by button to lookup words
def search(resultsArea):
    word = entry.get()
    if len(word) > 0 :
        result = lookUp(word)
        
        
        for meaning in result["meanings"]:
            
            partOfSpeech = ttk.Label(resultsArea, text=meaning['partOfSpeech'], wraplength=600) 
            partOfSpeech.pack(pady=10)
            
            definitions = "\n".join([defDict['definition'] for defDict in meaning['definitions']])
            definition = ttk.Label(resultsArea, text=definitions, wraplength=600) 
            definition.pack(pady=10)

def play_audio():
    text = entry.get()
    tts = gTTS(text)
    tts.save(text)

    pygame.mixer.music.load(text)
    pygame.mixer.music.play()


root = ttk.Window() # same as tk.Tk() from tkinter

# enabling scrolling
mainLayout = ScrolledFrame(root, autohide=True)
mainLayout.pack(fill=BOTH, expand=YES, padx=10, pady=10)

style = ttk.Style("litera") # setting theme for the interface
style.configure("Outline.TButton", font=("Arial", 12, "bold"), padding=10, relief=RAISED) # setting style for buttons
style.configure('TEntry', font=('Helvetica', 18), padding=10, relief=RAISED) # setting style for entry field

root.title("Dictionary")
root.geometry("600x400")
root.config(bg='grey')
# Banner
banner = ttk.Frame(root)
banner.pack(pady=20)

# Logo
logo = tk.PhotoImage(file="images/logo.png")
logoLabel = ttk.Label(mainLayout, image=logo)
logoLabel.pack(pady=10)

# Welcome message
welcome = ttk.Label(mainLayout, text="Welcome !", font=("Arial", 30, "bold"))
welcome.pack(pady=10)

# Search Box Frame
searchBox = ttk.Frame(mainLayout)
searchBox.pack(pady=20)

# Entry field
entry = ttk.Entry(searchBox, width=50, font=("Arial", 12))
entry.pack(side=LEFT, padx=5)

# Button
button = ttk.Button(searchBox, text="Look Up", command=lambda: search(mainLayout), style='Outline.TButton')
button.pack(side=RIGHT, padx=5)

voice_btn = ttk.Button(searchBox, text='voice', command=play_audio)
voice_btn.pack()

root.mainloop()
