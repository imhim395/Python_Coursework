computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"
print(computers)#since the key Lenovo is not present, it will add the new key and value to the dictionary, but we can do this faster

computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
computers.setdefault("Lenovo", "IdeaPad")#this method does the same thing as above but faster