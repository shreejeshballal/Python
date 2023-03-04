number = int(input("Enter the number:"))

for i in range(1,int(number/2)):
    if(number % i ==0):
        print("It is not a prime number")
        exit()
print("It is a prime number") 