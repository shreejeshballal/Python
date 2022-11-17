#To manipulate the string characters 
#join() method and split() method

str1 = "This is a string"

newStr1 = str1.split(" ")
newStr1[2] = "A"

def convertList(S):
    conStr= " "
    return conStr.join(S)

print(convertList(newStr1))


#2nd way using string indexing
print(str1[:8]+"A"+str1[9:])


str2 = "This is my book"
print("t"+str2[1:])

print('123ab'.islower())
print("hello23@}z |".isascii())