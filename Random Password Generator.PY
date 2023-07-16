
# # Code Clause internship

# # project 1

# # random password generator


# # METHOD 1

# import random

# # we use here lower,upper,special characters to generate a password

# lower="abcdefghijklmnopqrstuvwxyz"

# upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# numbers="1234567890"

# symbols="!@#$%&*"

# # Enter the required password length
# length_password = int(input("Enter length of password:"))

# all=lower+upper+numbers+symbols


# # length=9

# for i in range(5):

#     password="".join(random.sample(all,length_password))

#     print(f"Your password is {password}")


# METHOD 2


import random
import string

def generate_pwd(min_length, numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters= letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd= ""
    meets_criteria = False
    has_no = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_no = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_no
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enetr the length of Password:"))
has_no = input("Do you want numbers in your password Click (y/n)?").lower() == "y"
has_special = input("Do you want special characters click (y/n)?").lower() == "y"
pwd = generate_pwd(min_length,has_no,has_special)
print("Your generated password is:",pwd)
