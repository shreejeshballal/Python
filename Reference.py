x=[1,2,3]
y=x
x[2]=10
print(id(x) ,id(y))
print(x,y)
x=[4,5,6]
print(id(x) ,id(y))  #id() used to find memory address
print(x,y)

x=[1,2,3]
y=x
del x[0]
x=[5,6]
print(x,y)


#when it comes to primary data types like int char float they are sent to a function as copy ie pass by copy whereas when it comes to datatype like list,array then the address of the variable is passed

def addsomething(x):
    x.append(4)

def dosomething(y):
    y+=5

x=[1,2,3]
addsomething(x) #pass by reference
print(x)
y=5
dosomething(y)  #pass by value
print(y)   

