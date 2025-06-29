words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
temp={}
for i in words:
if i in temp:
temp[i]+=1
else:
temp[i]=1
print(temp)
