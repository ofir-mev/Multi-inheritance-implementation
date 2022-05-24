


def make_instance(cls):
        """Return a new object instance, which is a dispatch dictionary."""
        def get_value(name):
            if name in attributes:
                return attributes[name]
            else:
                value = cls['get'](name)
                return bind_method(value, instance)
        def set_value(name, value):
                attributes[name] = value
        attributes = {}
        instance = {'get': get_value, 'set': set_value}
        return instance

def bind_method(value, instance):
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value

def make_class(attributes, base_class=None,base_class2=None):
        """Return a new class, which is a dispatch dictionary."""
        def get_value(name):
            if name in attributes:
                return attributes[name]
            if base_class is not None:
                if callable(base_class['get'](name)):
                    return base_class['get'](name)
            if base_class2 is not None:
                if callable(base_class2['get'](name)):
                 return base_class2['get'](name)
        def set_value(name, value,*args):
            attributes[name] = value
        def new(*args):
            return init_instance(cls, *args)
        cls = {'get': get_value, 'set': set_value, 'new': new}
        return cls

def init_instance(cls, *args):
        """Return a new object with type cls, initialized with args."""
        instance = make_instance(cls)
        init = cls['get']('__init__')
        if init:
            init(instance, *args)
        return instance

def make_MyDate_class():
    def __init__(self, year,day=0,month=0):
        self['set']('Year', year)
        self['set']('Day', day)
        self['set']('Month', month)

    def setDay(self, day):
        if day >=1 and day <=30:
           self['set']('Day',day)
        else:
            print("day not in range")

    def getDay(self):
        return self['get']('Day')

    def setYear(self, year):
        if year >= 1900 and year <= 2100:
           self['set']('Year', year)
        else:
            print("year not in range")

    def getYear(self):
        return self['get']('Year')

    def setMonth(self, month):
        if month >= 1 and month <=12:
           self['set']('Month',month)
        else:
            print("month not in range")

    def getMonth(self):
        return self['get']('Month')

    def str(self):
        print(self['get']('Day'),"." ,self['get']('Month'),".",self['get']('Year'))

    def repr(self):
        return self

    return make_class(locals())


def make_MyPerson_class():
     def __init__(self, name,family,mydate,id):
        self['set']('Firstname', name)
        self['set']('Familyname', family)
        self['set']('Day', mydate['get']('Day'))
        self['set']('Month', mydate['get']('Month'))
        self['set']('Year', mydate['get']('Year'))
        self['set']('ID', id)
        
     def setFirstname(self,name):
         self['set']('Firstname',name)

     def getFirstname(self):
         return self['get']('Firstname')

     def setFamilyname(self,family):
         self['set']('Familyname',family)

     def getFamilyname(self):
         return self['get']('Familyname')

     def setID(self,id):
         if id >0:
            self['set']('ID',id)
         else:
            print("Worng ID number")

     def getID(self):
         return self['get']('ID')

     def str(self):
          day=self['get']('Day')
          month=self['get']('Month')
          year=self['get']('Year')
          print("Name:",self['get']('Firstname'),self['get']('Familyname'))
          print("DoB:",day,".",month,".",year)
          print("ID:",self['get']('ID'))
          
          

     def repr(self):
        return self

     return make_class(locals(),date)

def make_MyStudent_class():
     def __init__(self):
        self['set']('Department', 0)
        self['set']('Avg', 0)
        self['set']('Seniority', 0)

     def setDepartment(self,dep):
        self['set']('Department',dep)

     def getDepartment(self):
         return self['get']('Department')

     def setAvg(self,avg):
        self['set']('Avg',avg)

     def getAvg(self):
         return self['get']('Avg')

     def setSeniority(self,sen):
        self['set']('Seniority',sen)

     def getSeniority(self):
         return self['get']('Seniority')

     def str(self):
        print(p1['get']('str')())
        print("Learning:",self['get']('Department'))
        print("Avg:",self['get']('Avg'))
        print("Seniority:",self['get']('Seniority'))

     def repr(self):
         return self

     return make_class(locals(),p1)


def make_MyFaculty_class():
     def __init__(self):
        self['set']('Teaching', 0)
        self['set']('Salary', 0)
        self['set']('Seniority', 0)

     def setTeaching(self,teach):
        self['set']('Teaching',teach)

     def getTeaching(self):
         return self['get']('Teaching')

     def setSalary(self,sal):
        self['set']('Salary',sal)

     def getSalary(self):
         return self['get']('Salary')

     def setSeniority(self,sen):
        self['set']('Seniority',sen)

     def getSeniority(self):
         return self['get']('Seniority')

     def str(self):
        print(p1['get']('str')())
        print("Teaching:",self['get']('Teaching'))
        print("Salary:",self['get']('Salary'))
        print("Seniority:",self['get']('Seniority'))

     def repr(self):
         return self

     return make_class(locals(),p1)


def make_MyTA_class():
     def __init__(self):
         print("")

     def str(self):
        print(f1['get']('str')())
        print(s1['get']('str')())

     
     return make_class(locals(),f1,s1)

class Rlist:
        empty = ()
        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest
        def __getitem__(self, i):
            if i == 0:
                return self.first
            else:
                return self.rest[i-1]
        def __len__(self):
            return 1 + len(self.rest)


class Rational:
   def __init__(self, numer, denom):
    self.numer = numer 
    self.denom = denom 
   def str_rat(self):
    return "{0}/{1}".format(self.numer, self.denom)
   def numer(self):
        return (self.numer)
   def denom(self):
        return (self.denom)



def apply(operator_name, x, y):
    if operator_name == "add" or operator_name == "+":
        if type(x)==int and type(y)==int:
             return sum_two_int(x,y)
        elif type(x)==Rational and type(y)==Rational:
             return sum_two_rat(x,y)
        elif type(x)==Rlist and type(y)==Rlist:
            return combining_two_lists(x,y)
        elif type(x)==Rlist and type(y)==str:
            return rat_and_list(x,y)
        elif type(x)==Rational and type(y)==int:
            return sum_rat_and_int(x,y)
    elif operator_name == "mul" or operator_name == "*":
        if type(x)==int and type(y)==int:
             return mul_two_int(x,y)
        elif type(x)==Rational and type(y)==Rational:
             return rat_mul(x,y)
        elif type(x)==Rlist and type(y)==int:
            while y>1:
                x = rlist_and_int(x,x)
                y=y-1
            return x
        elif type(x)==Rational and type(y)==int:
            return mul_rat_and_int(x,y)

def rat_and_list(s, t):
        if s is Rlist.empty:
            return Rlist(t)
        else:
            return Rlist(s.first, rat_and_list(s.rest, t))

def combining_two_lists(l1, l2):
        if l1 is Rlist.empty:
            return l2
        else:
            return Rlist(l1.first, combining_two_lists(l1.rest, l2))

    
def sum_two_rat(r1,r2):
    nx, dx = r1.numer, r1.denom
    ny, dy = r2.numer, r2.denom
    return "{0}/{1}".format(nx * dy + ny * dx, dx * dy)


def sum_two_int(x,y):
    return x + y

def sum_rat_and_int(rat,x):
    nx, dx = rat.numer, rat.denom
    return "{0}/{1}".format(nx * 1 + x * dx, dx * 1)

def expression(s):
        if s.rest is Rlist.empty:
            rest = ''
        else:
            rest = ', ' + expression(s.rest)
        return 'Rlist({0}{1})'.format(s.first, rest)


def rlist_and_int(l1,l2):
    if l1 is Rlist.empty:
       return l2
    else:
        return Rlist(l1.first, rlist_and_int(l1.rest,l2))
    


def rat_mul(rat1,rat2):
    return "{0}/{1}".format(rat1.numer * rat2.numer, rat1.denom *rat2.denom)

def mul_two_int(x,y):
    return x * y

def mul_rat_and_int(rat,x):
    return "{0}/{1}".format(rat.numer * 1, rat.denom *x)

date = make_MyDate_class()
d1 = date['new']('2020','30','1')
person =make_MyPerson_class()
p1=person['new']('ofir','mev',d1,34544)
student = make_MyStudent_class()
s1=student['new']()
faculty=make_MyFaculty_class()
f1= faculty['new']()
TA=make_MyTA_class()
t1= TA['new']()
num1 = 2
num2 = 8

print("---mydate---:")
d1['get']('str')()
print("---person---:")
p1['get']('str')()
print("---student---:")
s1['get']('str')()
print("---faculty---:")
f1['get']('str')()
print("---TA---:")
t1['get']('str')()

ra1= Rational(1,3)
ra2= Rational(1,3)
rat = ra1.str_rat()
list1 = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
list2 = Rlist(7, Rlist(9, Rlist(8, Rlist(6))))

#add
print("add:\n")
print(expression(apply('add',list1,rat)))
print(expression(apply('add',list1,list2)))
print(apply('add',ra1,ra2))
print(apply("add",num1,num2))
print(apply("add",ra1,num1))

#mul
print("\nmul:\n")
print(expression(apply('mul',list1,num1)))
print(apply('mul',ra1,ra2))
print(apply("mul",num1,num2))
print(apply('mul',ra1,num1))
