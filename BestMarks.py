#Python program to find the best of two test average marks out of three test marks accepted from the user

m1,m2,m3 = [int(x) for x in input("Enter three marks:").split()]
if m1 > m2:
    if m2 > m3:
        print("Best Average: ",(m1+m2)/2)
    else:
        print("Best Average: ",(m1+m3)/2)
elif m1>m3:
    print("Best Average: ",(m1+m2)/2)
else:
    print("Best Average: ",(m2+m3)/2)

        

