input = open('input.txt', 'r')

# Part 1
overlap = {}
for line in input.read().strip().split('\n'):
    start, end = [list(map(int, side.split(','))) for side in line.split(' -> ')]
    if start[0] == end[0] or start[1] == end[1]:
        minX = min(start[0], end[0])
        maxX = max(start[0], end[0])
        minY = min(start[1], end[1])
        maxY = max(start[1], end[1])
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                point = (x, y)
                if point not in overlap:
                    overlap[point] = 0
                overlap[point] += 1

print(sum(1 for item in overlap.items() if item[1] >= 2))

overlap = {}

# Part 2
input = open('input.txt', 'r')
for line in input.read().strip().split('\n'):
    start, end = [list(map(int, side.split(','))) for side in line.split(' -> ')]
    minX = min(start[0], end[0])
    maxX = max(start[0], end[0])
    minY = min(start[1], end[1])
    maxY = max(start[1], end[1])
    if start[0] == end[0] or start[1] == end[1]:
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                point = (x, y)
                if point not in overlap:
                    overlap[point] = 0
                overlap[point] += 1
        continue
    dx = 1 if end[0] > start[0] else -1
    dy = 1 if end[1] > start[1] else -1
    x = start[0]
    y = start[1]
    while x != end[0] and y != end[1]:
        point = (x, y)
        if point not in overlap:
            overlap[point] = 0
        overlap[point] += 1
        x += dx
        y += dy
    point = (x, y)
    if point not in overlap:
        overlap[point] = 0
    overlap[point] += 1

print(sum(1 for item in overlap.items() if item[1] >= 2))
