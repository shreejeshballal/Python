import random

count=0
my_list = ["Hello","Hi","Making","Moshi"]


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



def get_word():
   
    choice = random.choice(my_list)
    print("The word has",len(choice),"letters")
    print("-----------------------------")
    print("START GUESSING!")
    for x in choice:
        print("_",end=" ")
    print("\n\n--------------------------------")
    return choice.upper()





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


    

def display():
 
    for x in word_alphabets:
        if x in correct_letters:
            print(x,end=" ")
            continue
        else:
            print("_",end=" ")
            continue
    hang()
    print("\n-----------------------------")
        
  


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
        print("------------------------")
        print("GAME OVER! YOU ARE HANGED")



def hangman():

    global word
    global count
    global user_letter
    global correct_letters
    global word_alphabets
    global used_letters


    word=get_word()
    wrong_letters=[]
    used_letters=[]
    correct_letters=[ ]
 
    word_alphabets = list(word)
    while int(count)<6:
        user_letter = input("Guess the letter:").upper()
        print("---------------------------")
        if user_letter.isalpha():
            if user_letter in used_letters:
                print("The letter has been already used")
            else:
                check_letter(user_letter)

            if len(word) == len(correct_letters):
                print("Congratulations! You have won!")
                return

        else:
            print("Enter a valid character!")
            print("------------------------")



hangman()


















