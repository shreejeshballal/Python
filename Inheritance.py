class Person:
    ''' '''
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    '''Inherited '''
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)


x= Student("Chiranth","Olsen")
x.printname()