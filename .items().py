birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years.items())#gives a list of tuples with the key and value, tuple is a data type like a list but it's immutable

for key, value in birth_years.items():
    print(key, value)#returns both keys and values