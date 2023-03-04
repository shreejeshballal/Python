# Make a list of first 10 letters of the Alphabet then using the slice operation do the following Print the first five letters of the list Print all the letters in even indices Print the letters from the 5th index to the end of the list 

sentence = input("Enter a sentence:")
alpha_list = list(sentence[:10])

print("First 5 letters of list: ",alpha_list[:5])

print("Letters in even indices are: ",end=" ")
for i in range(0,10,2):
    print(alpha_list[i],end=" ")

print("\nLetters from 5th index to end: ",alpha_list[5:])
