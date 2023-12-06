#!/usr/bin/env python3
from colorama import init, Fore
from mimesis import Person
from person import PersonGenerator
import os
import sys
import yagmail
from time import sleep
init()
pn = Person
person_data = PersonGenerator()



while True:
    what_generate = input("What generate: ")
    if what_generate.lower() == "person":
        personal_data = person_data.get_personal_data()
        do_you_want_create_output_file = input("Do you wanna create output file? \nY/n: ")
        if do_you_want_create_output_file.lower() == "y":
            os.system('type nul > output_file.txt')
            os.system(f"echo Output: {personal_data} > output_file")
            print(personal_data)
            print("You can type 'exit' for close the program.\n")
        elif do_you_want_create_output_file == "send on email":
            print("Sending...\n")
            sleep(3)
            yag = yagmail.SMTP(user='oneilheidy77@gmail.com', password='L@X123456789')
            yag.send(to='nedlauceby@gmail.com', subject='FAKE DATA', contents='its email from ur program mftdg open the output.txt for find the imformation. ', attachments='C:/mfdtg/output.txt')
            print("Type exit. For close the program. \n")

        else:
            print(personal_data)
    elif what_generate.lower() == "exit":
        print("Closing...")
        sys.exit()
    else:
        print(Fore.RED )
        print("Invalid input !!!")
        print(Fore.WHITE)
        print("Try person/Person ")
