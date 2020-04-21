#swap two elements in a list
list1=[1,2,3,4,5]
pos1=1
pos2=2
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print(list1)
#Output:
#[5, 2, 3, 4, 1]