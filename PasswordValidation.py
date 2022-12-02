#Develop a program to check the validity of the passwords read by a user, The following criteria should be used to check the validity. Password should have atleast,One Lowercase letter One Uppercase letter One Digit One Special Character Minimum 7 characters Program should accept the password as input and check against the criteria specified above. Print Valid or Invalid accordingly.

user_input = input("Enter the password:")

lower = upper = digit = special = length = 0 

if len(user_input) > 6:
    length = 1
    for char in user_input:
        if char.isupper():
            upper = 1
        elif char.islower():
            lower = 1
        elif char.isdigit():
            digit = 1
        else:
            special =1

if lower == upper == digit == special == length == 1:
    print("Valid Password")
else:
    print("Invalid Password")
