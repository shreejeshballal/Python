# Develop  a  python  script  to  maintain  an  employee  database  using  dictionary  with EmpID  as  key  and  EmpName,  EmpSal,  and  EmpAge  as  values  and  facilitate  the following usecases, Insert ‘n’ employee details into the dictionary reading ‘n’ as input. Check if an employee detail exists by reading EmpID as key. Display the details of an employee who fetches maximum salary. Note: Use Pretty Printing to display the results on console

emp_DB = {}

n = int(input("Enter the value for n: "))
def keyChecker(k):
    if int(k) in emp_DB:
            nk=int(input("The key already exits!. Enter a new one:"))
            keyChecker(nk)
    else:
        nk = k
    return nk
    
    
while n!=0:
    key,name,sal,age = input("Enter EmpID,EmpName,EmpSal,EmpAge seperated by ',':- ").split(",")
    value = [name,sal,age]
    nkey=keyChecker(key)
    emp_DB[int(nkey)] = value
    n-=1          

max_salary =0

for k in emp_DB.keys() :
    if max_salary < int(emp_DB[k][1]) :
        max_salary = int(emp_DB[k][1])
        key = k

print("The Details of the EMployee who fetches maximum salary is :- ",end=" ")
print(emp_DB[key])
