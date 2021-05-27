# This program will create a password for you
import random
import string

def new_password():

    lower_case_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    special_chars = ["!","@","#","$","%","^","*","&"]
    special_chars_clean = ""
    special_chars_clean_str = special_chars_clean.join(special_chars)
    numbers = string.digits

    all_sings = special_chars_clean_str + capital_letters + lower_case_letters + numbers
    letters = lower_case_letters + capital_letters
    password = []


    def password_generator():
        strenght_of_password = input('Hi! This is a password generator that will create unique password for you,'
                                    'for strong password type "S", for easy password type "E": ')
        
        if strenght_of_password[0].lower() == "e":
            number_of_chars = int(input("How many characters you need? "))
            for i  in range(number_of_chars):
                random_character = random.choice(letters)
                password.append(random_character)
        if strenght_of_password[0].lower() == "s":
            number_of_chars = int(input("How many characters you need? "))
            for i  in range(number_of_chars):
                random_character = random.choice(all_sings)
                password.append(random_character)


    # password_generator()

    def list_to_str(password):
        str1 = ''
        return (str1.join(password))

    print(f"This is your password: {list_to_str(password)}")


