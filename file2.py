with open("users.csv","r") as file:
    users = []
    data = file.readlines()
    #print(data,end="")
    for line in data:
        users.append(line.strip().split(","))

print(users)

user = input("username? ")pwd  = input("password? ")
if [user,pwd] in users:
    print("correct!")
else:
    print("wrong!")