#!/usr/bin/env python3'
from tkinter import *
from tkinter import ttk

clicks = 0

def click_button():
    global clicks
    clicks = 1
    btn["text"] = f"Clicks {clicks}"
    label = Label(text=f"{}")


root = Tk()
root.title("App title")
root.geometry('1024x760')

btn = ttk.Button(text="Click me!", command=click_button)
btn.pack()

root.mainloop()