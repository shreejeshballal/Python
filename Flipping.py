#python program to read a number A which contains only digits 0's and 1's. Check if it is possible to make all the digits same by just flipping one digit.Print 'YES' if flipping results in making all digits same else print 'NO'.

user_number = input("Enter a number which contains only 0's and 1's:")
user_number_list = list(user_number)
count0=0
count1=0
for num in user_number_list:
        if int(num) == 0:
            count0+=1
        else:
            count1+=1
if count0 == 1 or count1 == 1:
    print("YES")
else:
    print("NO")
