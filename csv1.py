outfile = open("m12.csv", "w")
for i in range(1, 11):
    outfile.write(str(i) + ',' + str(i*12))
    outfile.write('\n')
outfile.close()
