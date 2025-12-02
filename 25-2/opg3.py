import re

with open("Data.txt", "r") as file:
    for line in file:
        split = re.split(r'[,-]', line)
        
        for x in split:
            print([int(x)])