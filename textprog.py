with open("textfile.txt", "r") as inp:
    data = inp.readlines()
    for line in data:
        if "3" in line:
            print(line,end="")
'''
out = open("outfile.txt", "w")
for line in data:
   if not "3" in line:
      out.writelines(line.upper())
out.close()

out = open("outfile.txt", "a")
out.writelines("\nNew last line")
out.close()

'''