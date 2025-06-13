Strings
Slicing

x="Sample"
print(x.capitalize())
print(x.replace('a','A'))
print(x.replace('Sa','SA'))
my_list=x.split(' ')
print(my_list)

file="raw_data.csv"
if (file.endswith(".csv")):
print("CSV File")

file="raw_data.csv"
if (file.startswith("raw")):
print("Raw File")

statement="Hello Sample, Welcome Weekend Sample!"
print(statement.count("Sample"))

demo_str="Hello"
demo_var="10"
print(demo_str.isnumeric())
print(demo_var.isnumeric())
demo_alnum="10abc"
print(demo_alnum.isalnum())

x=10
if (x==10):
print("Matched")
elif (x>100):
if ((x>100) & (x<200)):
print("Incorrect")
else:
print("Greater than 200")
else:
print("X is not 10")

for i in range(1,10):
print(i)

my_list=["order","products","customers"]
for i in my_list:
if (i.lower() =="order"):
print("Table Order")
else:
print("No Table Order")

for i in my_list:
print(i)
for x in i:
print(x)

for i in my_list:
print(i)
if (i.lower()=="order"):
break
print(i) #it will not execute this

for i in my_list:
print(i)
if (i.lower()=="order"):
continue
print("continue",i)

for i in my_list:
print(i)
if (i.lower()=="order"):
pass
print("pass",i)

x=1
while(x<11):
print(x)
x=x+1

x=1
while(1==1):
print("Hello")
x=x+1
if (x>10):
break
