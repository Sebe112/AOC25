temp = 0
total = 0

with open("Data.txt", "r") as file: 
    for line in file:
        for x in range(0, 100):
            for y in range(x + 1 , 100):
                if int(line[x]) * 10 + int(line[y]) > temp:
                    temp = int(line[x]) * 10 + int(line[y])
        total += temp
        temp = 0

print(total)