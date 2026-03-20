def fctcalc(num):
    returned = 1
    for item in range(num,1,-1):
        returned *= item
    return returned

print(fctcalc(3))
print(fctcalc(4))
print(fctcalc(5))
