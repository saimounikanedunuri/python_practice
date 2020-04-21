#interchange first and last element in a list
list1=[1,2,3,4,5]
temp=list1[0]
size=len(list1)
list1[0]=list1[size-1]
list1[size-1]=temp
print(list1)

#output:
#[5, 2, 3, 4, 1]