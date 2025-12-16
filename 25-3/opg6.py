total = 0

with open("Data.txt", "r") as file: 
    for line in file:
        i = 12
        tempstr = ""
        temp = 0
        n = 0
        xtemp = 1
        while(i != 0):
            for x in range(n, 100 - i + 1):
                if  int(line[x]) > temp:
                    temp = int(line[x])
                    xtemp = x
            tempstr += str(temp)
            n = xtemp + 1
            temp = 0
            i += -1
        total += int(tempstr)

print(total)