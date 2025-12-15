import re
i = 0
a = 0
b = 0
res = 0

with open("Data.txt", "r") as file:
    for line in file:
        split = re.split(r'[,-]', line)

        for x in split:
            if i % 2 == 0:
                a = int(x)
            else:
                b = int(x)
                for y in range(a, b + 1):
                    first_half  = str(y)[:len(str(y))//2]
                    second_half = str(y)[len(str(y))//2:]

                    if first_half == second_half:
                        res += y
            i +=1

print(res)