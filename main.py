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

# function used by button to lookup words
def search():
    word = entry.get()
    if len(word) > 0 :
        result = lookUp(word)
        print(result)

root = ttk.Window() # same as tk.Tk() from tkinter

style = ttk.Style("litera") # setting theme for the interface
style.configure("Outline.TButton", font=("Arial", 12, "bold"), padding=10, relief=RAISED) # setting style for buttons
style.configure('TEntry', font=('Helvetica', 18), padding=10, relief=RAISED) # setting style for entry field

root.title("Dictionary")
root.geometry("600x400")
root.resizable(False, False)

# Banner
banner = ttk.Frame(root)
banner.pack(pady=20)

# Logo
logo = tk.PhotoImage(file="images/logo.png")
logoLabel = ttk.Label(root, image=logo)
logoLabel.pack(pady=10)

# Welcome message
welcome = ttk.Label(root, text="Welcome !", font=("Arial", 30, "bold"))
welcome.pack(pady=10)

# Search Box Frame
searchBox = ttk.Frame(root)
searchBox.pack(pady=20)

# Entry field
entry = ttk.Entry(searchBox, width=50, font=("Arial", 12))
entry.pack(side=LEFT, padx=5)

# Button
button = ttk.Button(searchBox, text="Look Up", command=search, style='Outline.TButton')
button.pack(side=RIGHT, padx=5)
root.mainloop()
