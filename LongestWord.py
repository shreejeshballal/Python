n = int(input("Enter no of elements in list:"))
list = []
for i in range(0,n):
   a = str(input("Enter element:"))
   list.append(a)

longest = ''
for i in range(0,n):
   if(len(list[i])>len(str(longest))):
      longest = list[i]

print(longest)