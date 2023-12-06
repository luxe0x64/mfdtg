#!/usr/bin/env python3
from mimesis import Person
from mimesis import Gender
from date import DateTime
from colorama import init, Fore
person = Person()
init()
#####################################################################
#                                                                   #
#                                                                   #
#                  Created by: nobody3132/luxe0x64                  #
#                                                                   #
#                                                                   #
#                                                                   #
#                                                                   #
#                                                                   #
#####################################################################

class PersonGenerator:
    full_name = person.full_name(gender=Gender.MALE)
    data = DateTime()
    birth_date = data.get_birth_date()
    email = person.email(domains=['gmail.com'])
    data_person = full_name, birth_date, email
    full_data_personal = f"Full name: {full_name} Birth Date: {birth_date} Email: {email} "

    def get_personal_data(self):
        return self.full_data_personal