import copy
lis = [1,2,3,4,5]
hi = copy.deepcopy(lis)
hi[2] = 4#only changes hi
print(lis)#deepcopy copies the list and returns a new list with same elements as lis.
print(hi)