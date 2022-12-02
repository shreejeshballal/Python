# Develop a python script to find the sum of all the even numbers in the given range

try:
    user_range = int(input("Enter a range for the sum:"))
except:
    print("Enter an integer!")
sum = 0
for i in range(1,user_range):
    if i % 2 == 0 :
        sum = sum + i
print("The sum of all even numbers in the given range is :",sum)
