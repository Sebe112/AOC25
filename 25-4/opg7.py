result = 0

def check_grid(char_2d_array, x, y):
    temp = 0
    grid_list = []

    if y + 1 < len(char_2d_array) and x + 1 < len(char_2d_array[y]):
        grid_list.append(char_2d_array[y + 1][x + 1])
    if y + 1 < len(char_2d_array):
        grid_list.append(char_2d_array[y + 1][x])
    if y + 1 < len(char_2d_array) and x - 1 >= 0:
        grid_list.append(char_2d_array[y + 1][x - 1])

    if y - 1 >= 0 and x + 1 < len(char_2d_array[y]):
        grid_list.append(char_2d_array[y - 1][x + 1])
    if y - 1 >= 0:
        grid_list.append(char_2d_array[y - 1][x])
    if y - 1 >= 0 and x - 1 >= 0:
        grid_list.append(char_2d_array[y - 1][x - 1])

    if x + 1 < len(char_2d_array[y]):
        grid_list.append(char_2d_array[y][x + 1])
    if x - 1 >= 0:
        grid_list.append(char_2d_array[y][x - 1])

    for i in range(len(grid_list)):
        if grid_list[i] == "@":
            temp += 1

    if temp > 3:
        return False
    else:
        return True


with open("Data.txt", "r") as file:
    char_2d_array = [list(line.strip()) for line in file if line.strip()]

    for y in range(len(char_2d_array)):
        for x in range(len(char_2d_array[y])):
            if char_2d_array[y][x] == "@":
                if check_grid(char_2d_array, x, y):
                    result += 1

print(result)
