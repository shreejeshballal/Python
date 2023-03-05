#program in Python to prompt for a string and then count the frequency of letters in the string and display the letter and its frequency in ascending order of its frequency.

string = input("Enter a string:")
freq = {}
sortedFreq={}
for char in string:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1

sortedValue = list(freq.values())
sortedValue.sort()

for i in sortedValue:
    for char in freq:
        if freq[char] == i:
            sortedFreq[char] = i

            
print(sortedFreq)

