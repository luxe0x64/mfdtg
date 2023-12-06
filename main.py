#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

import yagmail
from mimesis import Person
from person import PersonGenerator
import os
import sys
person = Person()


def output_file_alert_windows():
    label["text"] = entry.get
    label["text"] = "Output File Created."

def output_file_for_linux():
    os.system('touch output_file.txt')
    os.system(f"echo 'Output: {personal_data}' > output_file.txt")
    os.system('open output_file.txt')
    label["text"] = "Output File Created."
def show_message():
    label["text"] = entry.get
    label["text"] = f"{personal_data}"


def output_file():
    label["text"] = entry_output_file.get
    os.system('type nul > output_file.txt')
    os.system(f'echo {personal_data} > output_file.txt')
    os.system('start output_file.txt')
    label["text"] = "Output File Created."

def exit():
    sys.exit()

root = Tk() # Create the window
root.title("misha's fake data generator")  # Set the apple title like website 'Google'
root.geometry("1024x760")

label = Label(text="What generate?")
label.pack()

entry_exit = ttk.Entry()
entry_output_file = ttk.Entry()
entry = ttk.Entry()
btn_output_file = ttk.Button(text="Output File", command=output_file)
btn_output_file.pack(anchor=CENTER, padx=6, pady=6)
btn_exit = ttk.Button(text="Exit", command=exit)
btn_exit.pack(anchor=CENTER, padx=6, pady=6)
btn_output_file_linux = ttk.Button(text="Output File for Linux", command=output_file_for_linux)
btn_output_file_linux.pack(anchor=CENTER, padx=6, pady=6)

btn = ttk.Button(text="Person", command=show_message)
btn.pack(anchor=CENTER, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=CENTER, padx=6, pady=6)

data_person = PersonGenerator()
personal_data = data_person.get_personal_data()


root.mainloop()
