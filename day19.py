from collections import Counter, deque
from itertools import product

input = open('input.txt', 'r')
lines = input.read()

scanners = []
for scanner in lines.split('\n\n'):
    beacons = []
    for beacon in scanner.split('\n')[1:]:
        beacons.append(tuple(map(int, beacon.split(','))))
    scanners.append(beacons)


def align(scanner1, scanner2):
    points = []
    offset = []
    solved = set()
    for dimension in range(3):
        current = [beacon[dimension] for beacon in scanner1]
        for axis, flip in product((0, 1, 2), (1, -1)):
            if axis in solved:
                continue
            orientation = [beacon[axis] * flip for beacon in scanner2]
            shift = [b - a for (a, b) in product(current, orientation)]
            common, count = Counter(shift).most_common(1)[0]
            if count >= 12:
                break
        if count < 12:
            return False, False
        solved.add(axis)
        points.append([v - common for v in orientation])
        offset.append(common)
    return list(zip(*points)), offset


def findBeacons():
    result = set()
    stack = [scanners[0]]
    q = deque(scanners[1:])
    offsets = []
    while stack:
        scanner1 = stack.pop()
        for i in range(len(q)):
            scanner2 = q.popleft()
            updated, offset = align(scanner1, scanner2)
            if updated:
                stack.append(updated)
                offsets.append(offset)
            else:
                q.append(scanner2)
        result |= set(scanner1)
    return result, offsets


# Part 1
print(len(findBeacons()[0]))

# Part 2
offsets = findBeacons()[1]
result = 0
for a, b in product(offsets, offsets):
    current = sum(abs(x - y) for x, y in zip(a, b))
    result = max(result, current)
print(result)
