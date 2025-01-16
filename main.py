import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.icons import Icon
import requests

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
            
            meaningDict = result["phonetics"][result["meanings"].index(meaning)]
            
            if "text" in meaningDict.keys():
                phonetic = meaningDict["text"]
            else:
                phonetic = None
                
            audio = meaningDict["audio"]
            
            # frame for pronounciation
            soundBar = ttk.Frame(resultsArea)
            soundBar.pack(fill="x", padx=100)
            
            partOfSpeech = ttk.Label(soundBar, text=meaning['partOfSpeech'], justify="left", font=("Comic Sans MS", 13), style="info.TLabel") 
            partOfSpeech.grid(column=0, row=0)
            
            if phonetic != "" or phonetic != None:
                phonetics = ttk.Label(soundBar, text=phonetic, justify="left", font=("Comic Sans MS", 13), style="danger.TLabel")
                phonetics.grid(column=1, row=0)
            
            # audio
            audioIcon = tk.PhotoImage(file="./images/play.png", width=25, height=25)
            audio = ttk.Label(soundBar, image=audioIcon) 
            audio.grid(column=2, row=0)
            
            definitions = "\n\n".join([defDict['definition'] for defDict in meaning['definitions']])
            definition = ttk.Label(resultsArea, text=definitions, width=250, font=("Comic Sans MS", 16), wraplength=600, justify="left", padding=5) 
            definition.pack(pady=10, padx=100, anchor="center")

root = ttk.Window() # same as tk.Tk() from tkinter

# enabling scrolling
mainLayout = ScrolledFrame(root, autohide=True)
mainLayout.pack(fill=BOTH, expand=YES, anchor="center")

style = ttk.Style("litera") # setting theme for the interface
style.configure("Outline.TButton", font=("Comic Sans MS", 12, "bold"), padding=10) # setting style for buttons
style.configure('TEntry', font=('Helvetica', 18), padding=10) # setting style for entry field

root.title("Dictionary")
root.geometry("800x500")
root.resizable(False,False)

# Banner
banner = ttk.Frame(root)
banner.pack(pady=20)

# Logo
logo = tk.PhotoImage(file="images/book.png")
logoLabel = ttk.Label(mainLayout, image=logo)
logoLabel.pack(pady=10)

# Welcome message
welcome = ttk.Label(mainLayout, text="Look it up, genius!", font=("Comic Sans MS", 30))
welcome.pack(pady=10)

# Search Box Frame
searchBox = ttk.Frame(mainLayout)
searchBox.pack(pady=20)

# Entry field
entry = ttk.Entry(searchBox, width=60, font=("Comic Sans MS", 12))
entry.pack(side=LEFT, padx=5)

# Button
button = ttk.Button(searchBox, text="Look Up", command=lambda: search(mainLayout), style='Outline.TButton')
button.pack(side=RIGHT, padx=5)

root.mainloop()
