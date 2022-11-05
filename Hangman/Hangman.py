#----Required imports----#
import random

#----Reading from file-----
file= open(r"D:\\Python Dev\\Programs\\Hangman\WordList.txt",'r')
my_list=file.read().split(",")

#---Declarations----#
count=0
# my_list = ["Hello","Hi","Making","Moshi"]


#----Function used to get a word from the list of words defined above----#
def get_word():
    choice = random.choice(my_list)
    print("The word has",len(choice),"letters")
    print("--------------------------------")
    print("START GUESSING!")
    for x in choice:
        print("_",end=" ")
    print("\n\n--------------------------------")
    return choice.upper()


#-----Function to check whether the letter entered by the user exists in the word to be guessed----#
def check_letter(a):
    global count
    if a in word_alphabets:
        correct_letters.append(a)
        used_letters.append(a)
        print("BRAVO! You are on the right path...")
        display()
    else:
        used_letters.append(a)
        print("HaHa! You are about to die soon....")
        count+=1
        display()
    

#-----Function to display the respective output depending on the user's input----#
def display():
    for x in word_alphabets:
        if x in correct_letters:
            print(x,end=" ")
            continue
        else:
            print("_",end=" ")
            continue
    hang()
    print("--------------------------------")
        

#----Function to display the hangman body with respect to the error count-----#
def hang():
    global count
    if count==0:
        print()
        print("      _____")
        print("     |     |")
        print("     |     ")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")
    elif count==1:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")
    elif count==2:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |     |")
        print("     |     |")
        print("     |")
        print("     |")
        print("   -----")
    elif count==3:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |    /|")
        print("     |     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")       
    elif count==4:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |    /|\\")
        print("     |     |")
        print("     |")
        print("     |")
        print("     |")
        print("   -----")       
    elif count==5:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |    /|\\")
        print("     |     |")
        print("     |    /")
        print("     |")
        print("   -----")       
    elif count==6:
        print()
        print("      _____")
        print("     |     |")
        print("     |     O")
        print("     |    /|\\")
        print("     |     |")
        print("     |    / \\")
        print("     |")
        print("   -----")       
        print("--------------------------------")
        print("GAME OVER! YOU ARE HANGED")
        print("The word is",word)


#----Major function of the program----#
def hangman():
    global word
    global count
    global user_letter
    global correct_letters
    global word_alphabets
    global used_letters
    global alphabets
   
    used_letters=[]
    correct_letters=[]
    
    word=get_word()
    
    word_alphabets = list(word)
    alphabets = list(set(word_alphabets))
    alphabets.sort()

    while int(count)<6:
        user_letter = input("Guess the letter:").upper()
        print("--------------------------------")
        if user_letter.isalpha():
            if user_letter in used_letters:
                print("The letter has been already used")
            else:
                check_letter(user_letter)
            correct_letters.sort()
            if correct_letters == alphabets:
                print("Congratulations! You have won!")
                return
        else:
            print("Enter a valid character!")
            print("--------------------------------")


#----Main function which governs the entry and exit of control to the program----#
def main():

    print("--------------------------------")
    print("WELCOME TO HANGMAN GAME")
    print("--------------------------------")
    print("      _____")
    print("     |     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("     |")
    print("   -----")
    print("--------------------------------")
    
    hangman()
    while True:
        # print("--------------------------------")
        choice = input("Would you like to try another time (Y/N)?:")
        print("--------------------------------")
        if choice == "N" or choice=="n":
            print("Thank you for playing!")
            break
        elif choice == "Y" or choice== "y":
            hangman()
        else:
            print("Invalid choice...")  

#---Calling main function- Start of the program execution----#
main()




















