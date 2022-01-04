import re as regex
from collections import Counter

input = open('input.txt', 'r')
lines = input.read()

rebootSteps = []
for line in lines.split('\n'):
    state = int(line.split()[0] == 'on')
    x0, x1, y0, y1, z0, z1 = map(int, regex.findall('-?\d+', line))
    rebootSteps.append((state, x0, x1, y0, y1, z0, z1))


def overlap(cube1, cube2):
    x0, x1, y0, y1, z0, z1 = cube1
    i0, i1, j0, j1, k0, k1 = cube2
    xMax, yMax, zMax = (
        max(a, b) for a, b in
        zip((x0, y0, z0), (i0, j0, k0))
    )
    xMin, yMin, zMin = (
        min(a, b) for a, b in
        zip((x1, y1, z1), (i1, j1, k1))
    )
    if xMax <= xMin and yMax <= yMin and zMax <= zMin:
        return xMax, xMin, yMax, yMin, zMax, zMin
    return False


def toggle(step, cubes):
    state, current = step[0], step[1:]
    counter = Counter()
    for cube in cubes:
        doesOverlap = overlap(current, cube)
        if doesOverlap:
            counter[doesOverlap] -= cubes[cube]
    if state:
        cubes[current] = 1
    cubes.update(counter)
    return cubes


def calculateToggle(cubes):
    result = 0
    for key, value in cubes.items():
        x0, x1, y0, y1, z0, z1 = key
        size = (x1 + 1 - x0) * (y1 + 1 - y0) * (z1 + 1 - z0)
        result += size * value
    return result


# Part 1
cubes = Counter()
for step in rebootSteps:
    state, cur = step[0], step[1:]
    cur = overlap(cur, (-50, 50, -50, 50, -50, 50))
    if not cur:
        continue
    cubes = toggle((state, *cur), cubes)
print(calculateToggle(cubes))

# Part 2
cubes = Counter()
for step in rebootSteps:
    cubes = toggle(step, cubes)
print(calculateToggle(cubes))


