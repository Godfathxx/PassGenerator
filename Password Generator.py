"""
This is a script to generate strong passwords
"""

import random
import pyfiglet
import time

passchars = []
pass_ = ""

def gen_az_AZ_09() :
    global passchars
    global pass_
    max_sp_characters = 32
    strong_pass = False

    for _ in "1qQaAzZ2wWsSxX3eEdDcC4rRfFvV5tTgGbB6yYhHnN7uUjJmM8iIkK9oOlL0pP" :
        passchars.append(_)

    try : #taking control over random function
        seed_val = float(input("Enter seed value :"))
    except :
        seed_val = time.time_ns()
    finally :
        random.seed(seed_val)

    pass_len = int(input("Enter length of PASSWORD :"))
    special_chars = input("Enter a stream of allowed SPECIAL CHARACTERS :")

    special_chars_list = []

    if special_chars != "" :
        for _ in special_chars :
            for __ in range(max_sp_characters//len(special_chars)) :
                passchars.insert(random.randint(0,len(passchars)), _)
            special_chars_list.append(_)
    else : pass
    while not strong_pass :
        pass_ = ""
        for _ in range(pass_len) :
            pass_ += passchars[random.randint(0, len(passchars)-1)]
        strong_pass = chek_pass_strength(pass_, special_chars_list)
    save_pass()

def chek_pass_strength(password, special_characters) :
    strong_password = True
    for _ in special_characters :
        if _ not in password :
            strong_password = False
            return strong_password
        else : pass
    return strong_password

def save_pass() :
    global pass_
    try :
        file = open("pass.txt", "w")
        file.write(pass_)
        file.flush()
        file.close()
    except : 
        print("File operation failed")

def heading() :
    print(pyfiglet.figlet_format("PASS GEN", font="bulbhead"))
    print("* Characters a-z A-Z 0-9 are included\n")
    print("* You can restore your password by re-entering the")
    print("  seed value, the same password length and the same sequence of special characters")

heading()
gen_az_AZ_09()

print(pass_)
input()
