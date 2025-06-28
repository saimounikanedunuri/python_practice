str='AdEnhs'
#Converts it to lowercase.
str_lower=str.lower()
#print(str_lower)
#Removes all vowels (a, e, i, o, u).
vowel=['a','e','i','o','u']
for i in str_lower:
    #print(i)
    if i in vowel:
        #print(i)
        str_lower=str_lower.replace(i,'')
#Prints the resulting string.
print(str_lower)
