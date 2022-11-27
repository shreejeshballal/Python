#program in Python to prompt for a string and then count the frequency of letters in the string and display the letter and its frequency in ascending order of its frequency.

user_string = input("Enter the string:")
freq={}

for char in user_string:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1

freq_values = set(freq.values())

sorted_list = []
for i in freq_values:
    for char in freq:
        if freq[char]== i:
            sorted_list.append({char:i})
print(sorted_list)