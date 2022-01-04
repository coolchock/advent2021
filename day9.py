input = open('input.txt', 'r')

# Part 1
lines = input.read().splitlines()
total = 0
map = [[int(j) for j in i] for i in lines]
for i in range(len(map)):
    for j in range(len(map[i])):
        if all((row == i and column == j) or row < 0 or column < 0 or row >= len(map) or column >= len(map[i]) or
               map[i][j] < map[row][column] for row
               in range(i - 1, i + 2) for column in range(j - 1, j + 2)):
            total += map[i][j] + 1
print(total)


# Part 2
def visit(x, y):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[x]) or (x, y) in visited or map[x][y] == 9:
        return
    visited.add((x, y))
    visit(x - 1, y)
    visit(x + 1, y)
    visit(x, y - 1)
    visit(x, y + 1)


visited = set()
basins = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) not in visited and map[i][j] != 9:
            prev = len(visited)
            visit(i, j)
            basins.append(len(visited) - prev)
basins.sort()
print(basins[-3] * basins[-2] * basins[-1])
