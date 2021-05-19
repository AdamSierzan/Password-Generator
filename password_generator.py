# This program will create a password for you
import random
import string




lower_case_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
special_chars = string.punctuation
special_chars_clean = special_chars.replace("(", "", ")", "", "{", "", "}", "", "[", "", "]", "", "/", "")
# / \ ' " ` ~ , ; : . < > )
print(special_chars_clean)
# numbers = random.randint(0,9)
# all_sings = special_chars + capital_letters + lower_case_letters
# print(all_sings)
# password = []


# def password_generator():
#     number_of_chars = int(input("Hi! This is a password generator that will create unique password for you, type ""S"" for strong password, ""W"" for weak password: "))
#     for i  in range(number_of_chars):
        









# password_generator()




# def list_to_str(password):
#      str1 = ''
#      return (str1.join(password))

# print(list_to_str(password))

# # print(password)