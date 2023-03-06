import datetime

class birthday:
    """Representation of a birthday date"""

    def __init__(self,month=None,year=None,day=None):
        self.birthday = datetime.datetime(year, month, day)
    

    def __str__(self):
        return self.birthday.strftime("%d/%m/%y")
    

    def calculate_bday(self):
        now = datetime.datetime.now()
        diff = now-self.birthday
        print(diff)

p1 = birthday(10,2022,1)
print(p1)
birthday.calculate_bday(p1)
