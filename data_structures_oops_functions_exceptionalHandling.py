my_list=[1,2,'Sample','Code',['aa','bb','cc']]
print(my_list[0])
print(my_list[4][1])
print(my_list[-3:])
print(my_list[len(my_list)-3:len(my_list)])
print(my_list[-10:])

updated_list=[1,2,'Sample','Code',3,4,5,6]
print(updated_list)
print(updated_list[::2])
updated_list.append("Hello")
print(updated_list)
updated_list.insert(1,"Appended")
print(updated_list)
updated_list.pop()
print(updated_list)

another_list=[1,2,3,4,5,6]
another_list.reverse()
print(another_list)
for i in reversed(another_list):
    print(i)
print(another_list[::-1])

print(another_list[-3:])
print(another_list[:-1])

# list comprehension
new_list=[]
for i in another_list:
    new_list.append(i*i)
print(new_list)

my_list=[1,2,3,4,5,6]
new_list=[i*i for i in my_list if (i%2)==0]
print(new_list)
new_list=[i*i for i in my_list if (i%2)==0 if (i!=6)]
print(new_list)

# dictionary
my_dict={'x':1,'y':2,'z':3}
print(my_dict)

my_dict['x']=10
print(my_dict)

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

my_dict={'x':1,'y':2,'z':3,'demo':{'a':1,'b':2,'c':3}}
print(my_dict['demo']['b'])

# sets
a={1,2,3,4,5,2,3,4,5,6,7}
b={10,11,12,13,2,3,4}
print(a.union(b))

print(a.intersection(b))

c={}
print(type(c))

d=set()
print(type(d))

#tuple
my_tup=(1,2,3,4,5)
print(my_tup)

my_tuplist=list(my_tup)
print(my_tuplist)

my_tuplist.append(6)
print(my_tuplist)

my_tup=tuple(my_tuplist)
print(my_tup)

#functions
x=10
if (x>10):
    print("Greater than 10")
else:
    print("IDK")

x=20
if (x>10):
    print("Greater than 10")
else:
    print("IDK")

x=5
if (x>10):
    print("Greater than 10")
else:
    print("IDK")

x=10
def my_func():
    if (x>10):
        print("Greater than 10")
    else:
        print("IDK")
my_func()

def my_func(p_x):
    if (p_x>10):
        print("Greater than 10")
    else:
        print("IDK")
    return p_x
returned_val=my_func(20)
print(returned_val)

def my_func(p_x,p_y):
    print(p_x,p_y)
my_func(10,20)

def my_func(p_x,p_y=20):
    print(p_x,p_y)
my_func(10)

def my_func(p_x,p_y=20):
    print(p_x,p_y)
my_func(10,30)

def my_func(**p_x):
    print(p_x,type(p_x))
    print(p_x.keys())
my_func(x=10,y=20,z=30)

#lambda functions
def add(x,y):
    return x+y
var=add(10,20)
print(var)

addition=lambda x,y:x+y
var=addition(10,20)
print(var)

#map, filter, reduce
my_list=[1,2,3,4,5,6]

def square(p_x):
   
    ret_list=[i*i for i in p_x]
   
    print(ret_list)
square(my_list)

def square(p_x):
    return p_x*p_x
a_result=list(map(square,my_list))
print(a_result)
result=(map(square,my_list))
print(result)

my_list=[1,2,3,4,5]
def square(p_x):
    if(p_x %2==0):
        return p_x*p_x
result=list(map(square,my_list))
print(result) #[None, 4, None, 16, None]

result=list(filter(square,my_list))
print(result) #[2, 4]

from functools import reduce
def square(p_x,p_y):
    return p_x+p_y
result=(reduce(square,my_list))

print(result)

#Exception handling
x="10"
# if (x>10):
#     print("Greater than 10")
# else:
#     print("Bla Bla Bla")
# print("Hello World")

try:
    if (x>10):
        print("Greater than 10")
    else:
        print("Bla Bla Bla")
except:
    print("hey except block")

print("Hello!")


try:
    if (x>10):
        print("Greater than 10")
    else:
        print("Bla Bla Bla")
except Exception as e:
    print(e)

print("Hello!")

#strings
name='Angel'
str=f"Sample code here,{name} lets practice"
print(str)

x="10"
try:
    if (x>10):
        print("Greater than 10")
    else:
        print("Bla Bla Bla")
except Exception as e:
    print(f"Hey, here is your error - {e}")
finally:
    print("I will always run :)")
print("Hey!")

def my_func(p_x):
    print("Hey!")
    try:
        if (p_x % 2 ==0):
            return 1
    except Exception as e:
        return e
    print("Hey@") #this will not run
my_func(4)

def my_func(p_x):
    print("Hey!")
    try:
        if (p_x % 2 ==0):
            return 1
    except Exception as e:
        return e
    finally:
        print("Hey@")
my_func(4)



#global value
x=100
def my_func():
    x=5
    print(x)
my_func()

#custom error
# x=99
# if x<100:
#     raise Value Error("Value < 100 is not allowed")

x=99
if x<100:
    raise Exception("Value < 100 is not allowed")

#difference between Value Error and Exception

my_list=[100,200,300,400,500]
for i in my_list:
    print(i)
   
#enumerate
for i in enumerate(my_list):
    print(i)

#OOPs
class emp():
    emp_name='Sample' #variables in class are attributes
    emp_dept='IT'
   
    def info(self,emp_name,emp_dept): # functions in class are methods
        print(f"Emp {emp_name} works for {emp_dept}") #these var coming from class
       
emp1=emp()
# print(emp1.emp_name)
# print(emp1.emp_dept)

# emp1.info()
emp1.info("Replaced","IT")

# class emp():
#     emp_name='Sample' #variables in class are attributes
#     emp_dept='IT'
   
#     def info(self,emp_name,emp_dept): # functions in class are methods
#         print(f"Emp {self.emp_name} works for {self.emp_dept}") #these var coming from class
       
# emp1=emp()

# emp1.info("Replaced","IT")

class emp():
    emp_name='Sample' #variables in class are attributes
    emp_dept='IT'
   
    def info(self): # functions in class are methods
        print(f"Emp {self.emp_name} works for {self.emp_dept}") #these var coming from class
       
emp1=emp()
emp1.info()
emp.info(emp1)

#static, class, instance methods
class emp():
    comp='XYZ'
   
   
    def __init__(self,emp_name,emp_dept):
        self.emp_name=emp_name
        self.emp_dept=emp_dept
   
    #alternative to class method
    def changes(self,new_comp):
        emp.comp=new_comp #instance methods
   
    @classmethod
    def changesInClass(cls,new_comp):
        cls.comp_name=new_comp
       
    def info(self): #instance methods
        print(f"Emp {self.emp_name} works for {self.emp_dept} in {self.comp}")
       
    @staticmethod
    def add(x,y):
        print(x+y)
   
emp1=emp('Sample','IT')
emp2=emp('Another','HR')
emp1.info()
emp2.comp='ABC'
print(emp2.emp_name)
emp1.changesInClass("NewNewCompany")
print(emp1.comp_name)
emp2.info()

emp1.changes('New comp')
print(emp1.comp)
emp.comp='ABC'
emp1.info()

emp1.add(1,2)

#getters - get the values
#setters - set the instance attr
class emp():
    comp='XYZ'
   
   
    def __init__(self,emp_name,emp_dept):
        self.emp_name=emp_name
        self.emp_dept=emp_dept
       
    def info(self): #getter
        print(f"Emp {self.emp_name} works for {self.emp_dept} in {self.comp}")
   
    #setter
    def changeinfo(self,new_empname,new_empdept):
        self.emp_name=new_empname
        self.emp_dept=new_empdept
   
    @classmethod
    def changesInClass(cls,new_comp):
        cls.comp_name=new_comp
       
   
       
    @staticmethod
    def add(x,y):
        print(x+y)
   
emp1=emp('Sample','IT')
emp1.changeinfo('Sample','IT')
emp1.info()

#getters - get the values
#setters - set the instance attr
class emp():
    comp='XYZ'
   
   
    def __init__(self,emp_name,emp_dept):
        self.emp_name=emp_name
        self.emp_dept=emp_dept
       
    def info(self): #getter
        print(f"Emp {self.emp_name} works for {self.emp_dept} in {self.comp}")
   
    @property #getter
    def info(self):
        print(f"Emp {self.emp_name} works for {self.emp_dept} in {self.emp_name}")
   
    @info.setter
    def info(self,new_empdetails):
        new_empname=new_empdetails[0]
        new_empdept=new_empdetails[1]
       
        self.emp_name=new_empname
        self.emp_dept=new_empdept    
   
    #setter
    # def changeinfo(self,new_empname,new_empdept):
    #     self.emp_name=new_empname
    #     self.emp_dept=new_empdept
   
    @classmethod
    def changesInClass(cls,new_comp):
        cls.comp_name=new_comp
       
   
       
    @staticmethod
    def add(x,y):
        print(x+y)
   
emp1=emp('Sample','IT')
emp1.info=['Sample','HR'] #setter
print(emp1.info) #getter

#Inheretence
#single, multi level, multiple inheretence
#single inheretence
class comp():
    def comp_info(self):
        print("Company name is XYZ")
   
class emp(comp):
    def emp_info(self):
        print("EmpName is Sample")
       
emp1=emp()
emp1.comp_info()

#Inheretence
#single, multi level, multiple inheretence
#multi level
class comp():
    def __init__(self,comp_name):
        self.comp_name=comp_name
       
    def comp_info(self):
        print(f"Cpany name is {self.comp_name}")
   
class emp(comp):
    def __init__(self,emp_name,comp_name):
        self.emp_name=emp_name
        self.comp_name=comp_name
   
    def emp_info(self):
        print(f"Empname is {self.emp_name}")
       
emp1=emp('Sample','XYZ')
emp1.comp_info()
