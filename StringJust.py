# def spam():
#     global eggs
#     eggs=10
#     print( eggs)

# eggs = 50
# spam()
# eggs = 50
# print(eggs)
import pprint
def test(num):
    try:
        return 50/num
    except ZeroDivisionError:
        print("Zero Error")
        return "hello"

print(test(0))

ice = [['mango','apple','chikku'],[10,20,30],'yooo']
print(ice[1][1])

print(ice[0][-8:0])
for i in ice:
    print(i)

hello,chicken,meh= ice
print(meh)

rock = [1,2,3,4]
rock.insert(0,10)
print(rock)

string = "hello world"
listS = string.split()
print(listS)
listS1 = ' '
listS1.join(listS)
print(listS1)


t = ['hi','world','rock']

joinedS = "hi "
joinedS = joinedS.join(t)
print(joinedS)

cat = {'size':'large','breed':'local'}
print(cat['size'])

print(cat.values())

for i in cat.keys():
    print(cat[i])

pprint.pprint(cat)
print(pprint.pformat(cat))

side = " 1 hello 1 "
print(side.isalpha())

print(side.rjust(10,'*'))
print(side.ljust(10,'*'))
print(side.center(10,'*'))

print(side.strip())
print(side.rstrip())
print(side.lstrip())