#Python program to find whether the given number is a Perfect Number.

user_num = int(input("Enter a number:"))
sum = 0
for num in range(1,user_num//2+1):
    if user_num % num == 0:
        sum = sum + num
    if sum == user_num:
        print("The given number is a perfect number")
        break
if sum != user_num:
    print("The given number is not a perfect number")
