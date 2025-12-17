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

for r in ranges:
    result += r[1] - r[0]

print(result)