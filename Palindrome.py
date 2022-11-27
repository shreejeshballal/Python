#Python code snippet to check if a given string is Palindrome or not.(Without using string methods except len() )

user_string = input("Enter a string: ")
j=len(user_string)-1
i=0
while i<j:
    if user_string[i] == user_string[j]:
        i=i+1   
        j=j-1
    else:
        print("Given string is not a palindrome")
        break
if i == j:
    print("Given string is a palindrome")
    


    



