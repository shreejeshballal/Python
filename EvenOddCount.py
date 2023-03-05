n = int(input("Enter no of elements in list:"))
list = []

for i in range(n):
    try:
        list.append(int(input("Enter number:")))

    except Exception as e:
        print(e)
        list.append(int(input("Enter number:")))
even = 0
odd = 0
for i in list:
    if(i % 2 ==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)