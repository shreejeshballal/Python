class Time:
    """ Representtion of time object"""

    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
    # print(t.hour,":",t.minute,":",t.second)
        return('%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second))

    def __add__(self,t):
        sum = Time()
        sum.hour = self.hour+t.hour
        sum.minute = self.minute+t.minute
        sum.second = self.second+t.second

        if sum.second >=60:
            sum.second= sum.second-60
            sum.minute = sum.minute+1
        if sum.minute >=60:
            sum.minute = sum.minute-60
            sum.hour = sum.hour+1
        return sum

def increment_time(t,second):
    t.second = t.second + second
    if t.second >=60:
        t.second = t.second - 60
        t.minute = t.minute +1
    if t.minute >=60:
        t.minute = t.minute - 60
        t.hour = t.hour +1



t1 = Time()
t1.hour = 10
t1.minute = 30
t1.second = 15
print(t1)
t2 = Time()
t2.hour = 7
t2.minute = 5
t2.second = 20
print(t2)


print(t1+t2)



t4 = Time(13,5,20)
print(t4)