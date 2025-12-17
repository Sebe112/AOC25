ranges = []
numbers = []
result = 0

with open("Data.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if "-" in line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
        else:
            numbers.append(int(line))
            
for n in numbers:
    for r in ranges:
        if r[0] <= n <= r[1]:
            result += 1
            break  # count this number once

print(result)