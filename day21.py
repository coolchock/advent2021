from collections import deque
from functools import lru_cache
from itertools import product

playerOne = 7
playerTwo = 10

# Part 1
positions = [playerOne, playerTwo]
rolls = 0
q = deque(range(1, 101))
score = [0, 0]
turn = 0
while max(score) < 1000:
    move = sum(list(q)[:3])
    q.rotate(-3)
    rolls += 3
    positions[turn] = (positions[turn] + move - 1) % 10 + 1
    score[turn] += positions[turn]
    turn = 1 - turn
print(min(score) * rolls)


# Part 2
@lru_cache(None)
def splitUniverse(positions, scores=(0, 0), turn=0):
    currentPositions, currentScores = list(positions), list(scores)
    wins = [0, 0]
    for rolls in product((1, 2, 3), repeat=3):
        move = sum(rolls)
        currentPositions[turn] = (positions[turn] + move - 1) % 10 + 1
        currentScores[turn] = scores[turn] + currentPositions[turn]
        if currentScores[turn] >= 21:
            wins[turn] += 1
        else:
            one, two = splitUniverse(tuple(currentPositions), tuple(currentScores), 1 - turn)
            wins[0] += one
            wins[1] += two
    return wins


print(max(splitUniverse((playerOne, playerTwo))))
