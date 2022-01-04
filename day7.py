# Part 1
input = open('input.txt')
crabPositions = [int(crabPosition) for crabPosition in input.read().split(',')]
min = min(crabPositions)
max = max(crabPositions)

minCost = 9999999999999

cost = 0
for i in range(min, max + 1):
    cost = sum(abs(i - crabPosition) for crabPosition in crabPositions)
    if cost < minCost:
        minCost = cost

print(minCost)

# Part 2
minCost = 999999999999999


def moveCost(diff):
    return (diff * (diff + 1)) // 2


for i in range(min, max + 1):
    cost = sum(moveCost(abs(i - crabPosition)) for crabPosition in crabPositions)
    if cost < minCost:
        minCost = cost

print(minCost)
