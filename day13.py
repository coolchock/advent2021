import re as regex

input = open('input.txt', 'r')
dots = input.read()


def parse(dots):
    points = [(int(x), int(y)) for x, y in regex.findall(r'(\d+),(\d+)', dots)]
    folds = [(axis, int(n)) for axis, n in regex.findall(r'fold along ([xy])=(\d+)', dots)]
    return points, folds


dots, folds = parse(dots)


def fold(axis, line, dots):
    result = set()
    for x, y in dots:
        if axis == 'x':
            x = line - abs(x - line)
        else:
            y = line - abs(y - line)
        result.add((x, y))
    return result


# Part 1

visible = len(fold(*folds[0], set(dots)))
print(visible)

points = set(dots)
for foldInstruction in folds:
    points = fold(*foldInstruction, points)

xMax, yMax = max(x for x, y in points), max(y for x, y in points)

grid = [[' ' for x in range(xMax + 1)] for y in range(yMax + 1)]
for j, i in points:
    grid[i][j] = '#'

# Part 2
for row in grid:
    print(''.join(row))
