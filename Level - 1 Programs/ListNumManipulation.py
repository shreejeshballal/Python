#Python script which repeatedly reads numbers until the user enters “Finished” and stores them in a list. Once “Finished” is entered, print out the total,count, maximum and minimum of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to next number.

num_list = []
while True:
    num = input("Enter number | Enter 'Finished' to stop taking number:")
    if num == "Finished":
        break
    else:
        try:
            num_list.append(int(num))
        except:
            print("Error! Skipping to next number....")

print("Count :",len(num_list))

total = 0
for i in num_list:
    total = total + i
print("Total :",total) 

max = min = num_list[0]
for i in range(1,len(num_list)):
    if num_list[i] > max:
        max = num_list[i]
    elif num_list[i]< min:
        min = num_list[i]
print("Max :",max) 
print("Min :",min) 

