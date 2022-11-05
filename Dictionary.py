#Basic dictionary
my_dict={'name':'Sachin','Age':45}
print(my_dict)

#Access item in dictionary
print(my_dict['name']) #Syntax : dictionary_name["key"]

#item() used to get the each item in the dictionary in the form of tuple
birthday={"Alice":"April 22","Ram":"Dec 15","Frank":"Jan 1"}
for items in birthday.items():
    print(items)

#printing value and key of a dictionary separately
for K,V in birthday.items():
    print(K,":",V)

#key():to get list of all the keys of the dictionary
keys = birthday.keys()
print(keys)

#values():to get the values of eacch key of the dictionary
values = birthday.values()
print(values);[]

#Program to get birthday of a person from dictionary
while True:
    name = input("Enter a name:")
    if name == "":
        break
    if name in birthday:
        print(birthday[name]+ "is the birthday of "+name)
    else:  
        print("I do not have the information on "+name)
        bday = input("Enter the birthday of "+name)
        birthday[name]=bday
        print("Dictionary Updated")
        

