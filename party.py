names = []
names.append(input("name1"))
names.append(input("name2"))
names.append(input("name3"))

more = True
while more:
    names.append(input("name?"))
    more =(input("more? ") == "y")

print(names) 


