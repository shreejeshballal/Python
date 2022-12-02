#Write a program to find the sum and average of numbers inputted from the user byusing the concept of lists in Python

user_list = []

while True:
    item = input("Enter the Number [TYPE 'QUIT' TO STOP] :")
    if item == "QUIT":
        break
    else:
        try:
            user_list.append(int(item))
        except:
            print("Enter valid number!")

summ = avg = 0
for num in user_list:
    summ = summ + num
avg = summ/len(user_list)

print("Sum :",summ)
print("Average :",avg)