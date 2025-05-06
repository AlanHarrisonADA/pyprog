with open("file1.txt","r") as file:
    data = file.readlines()
    print("==============================")
    #print(data,end="")
    for line in data:
        print(line,end="")
    print("==============================")
    print()
