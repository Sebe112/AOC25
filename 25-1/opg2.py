import re

count = 0
dial = 50

with open("Data.txt", "r") as file:
    for line in file:
        L = re.split("L", line)
        R = re.split("R", line)
        if re.search("L", line):
            for x in range(int(L[1])):
                dial -= 1 
                if dial == 0:
                    count += 1
                if dial == -1:
                    dial = 99
        else:
            for x in range(int(R[1])):
                dial += 1
                if dial == 100:
                    count += 1
                    dial = 0

print(count)