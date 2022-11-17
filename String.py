#To manipulate the string characters 
#join() method and split() method

str1 = "This is a string"

newStr1 = str1.split(" ")
newStr1[2] = "A"

def convertList(S):
    conStr= " "
    return conStr.join(S)

print(convertList(newStr1))
