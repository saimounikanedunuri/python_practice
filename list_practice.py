#Sort the list in ascending order.
x=[11,21,1,2,12]
y=sorted(x)
print(y)

#Remove all duplicates from the list.
list1=[1,2,3,4,2,4,2]
result=set(list1)
res=list(result)
print(res)

#Sort the list in ascending order.
x=[11,21,1,2,12]
x.sort()
print(x)
why above worked but
print(x.sort()) #o/p: None
y=x.sort()
print(y) #None
why None for above 2 scenarios?

understood sort and sorted difference
