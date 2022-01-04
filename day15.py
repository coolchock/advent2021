import heapq

input = open('input.txt', 'r')
lines = input.read()

grid = []
for line in lines.split('\n'):
    grid.append(list(map(int, line)))

X = len(grid)
Y = len(grid[0])


def move(grid):
    row, column = len(grid), len(grid[0])
    costs = {}
    heap = [(0, 0, 0)]
    while heap:
        cost, x, y = heapq.heappop(heap)
        if (x, y) == (row - 1, column - 1):
            return cost
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < row and 0 <= ny < column:
                newCost = cost + grid[nx][ny]
                if costs.get((nx, ny), float('inf')) <= newCost:
                    continue
                costs[(nx, ny)] = newCost
                heapq.heappush(heap, (newCost, nx, ny))

# Part 1
print(move(grid))

# Part 2
row, column = len(grid) * 5, len(grid[0]) * 5
expanded = [[0 for column in range(column)] for row in range(row)]
for i in range(row):
    for j in range(column):
        dist = i // X + j // Y
        cur = grid[i % X][j % Y] + dist
        cur = cur % 9 or cur
        expanded[i][j] = cur

print(move(expanded))

