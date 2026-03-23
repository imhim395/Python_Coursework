set1 = {1,2,3,4}#no duplicates allowed, they will only appear once
set2 = set({1,2,3,4,5})#this is using set function
print(set1)
print(set2)
#for empty sets, u have to use set function or else python will think its a dictionary
set3 = set(range(1, 12, 2))#prints odd numbers 1-12
print(set3)
#sets can also hold different data types