#swap two elements in a list
list1=[1,2,3,4,5]
pos1=1
pos2=2
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print(list1)
#Output:
#[5, 2, 3, 4, 1]

list1=[1,2,3,4,5]
pos1=1
pos2=2
temp=list1[pos1]
list1[pos1]=list1[pos2]
list1[pos2]=temp
print(list1)
#output:
#[1,3,2,4,5]
