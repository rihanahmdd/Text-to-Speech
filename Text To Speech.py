import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3
import sys

win = tk.Tk()
win.geometry("410x390")
win.title("Text To Speech")
win.resizable(0,0)


# Creating Frame 
text_frame = ttk.Frame(win)

# Labels 
space_lbl = ttk.Label(win, width=10)
intro_lbl = ttk.Label(win, text="Text To Speech", font=("cambria", 15, 'bold'))

# Buttons
read_btn = ttk.Button(win, text="Read")
clear_btn = ttk.Button(win, text="Clear")
exit_btn = ttk.Button(win, text="Exit")

# Text Editor
text_editor = tk.Text(text_frame, width='45', height='15', relief=tk.RIDGE, bd='2', wrap='word')
text_editor.config(font=("cambria", 11,))
text_editor.focus_set()

# Scroll Bar
scrollbar = tk.Scrollbar(text_frame)
text_editor.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_editor.yview)


# Griding 
intro_lbl.grid(rowspan=3, columnspan=3, sticky=tk.E)
space_lbl.grid(row=0, column=0)
read_btn.grid(row=1, column=4, pady=5, sticky=tk.W)
text_frame.grid(row=3, columnspan=5, padx=20, pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(side=tk.LEFT)
clear_btn.grid(row=4, column=3, pady=10, sticky=tk.W)
exit_btn.grid(row=4, column=4, pady=10, sticky=tk.W)


################################### Fucationality ################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
male_voice = voices[0]
female_voice = voices[1]
engine.setProperty('voice', voices[0])

# Creating Speak Button
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def read_button():
    text = text_editor.get(1.0, tk.END)
    if len(text)==1:
        text = "Please, write something. Than I will Speak"
    speak(text)
    text_editor.focus_set()

def clear_button():
    text_editor.delete(1.0, tk.END)
    text_editor.focus_set()

def exit_button():
    win.destroy()


# binding Buttons
read_btn.config(command=read_button)
clear_btn.config(command=clear_button)
exit_btn.config(command=exit_button)



win.mainloop()


# Created and Programmed By Rihan Ahmed
