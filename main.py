import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests

def lookUp(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    results = response.json()

    result = dict({
        "phonetics": results[0]["phonetics"],
        "meanings": results[0]["meanings"],
    })

    return result


root = ttk.Window() # same as tk.Tk() from tkinter
style = ttk.Style("flatly") # setting theme for the interface
style.configure("TButton", font=("Arial", 12, "bold"), padding=10) # setting style for buttons
root.title("Dictionary")
root.geometry("600x400")
root.resizable(False, False)
root.mainloop()
