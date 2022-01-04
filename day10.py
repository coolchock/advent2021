# DONE
input = open('input.txt', 'r')

chunks = [line.rstrip('\n') for line in input.readlines()]

# Part 1
pairs = {'[': ']', '(': ')', '{': '}', '<': '>'}

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}


def corruptedScore(line):
    stack = []

    for chunk in line:
        if chunk in pairs:
            stack.append(chunk)

        else:
            if not stack:
                return scores[chunk]
            poppedChunk = stack.pop()
            if chunk != pairs[poppedChunk]:
                return scores[chunk]

    return 0


print(sum(corruptedScore(line) for line in chunks))

# Part 2

completeScores = {')': 1, ']': 2, '}': 3, '>': 4}


def getIncompleteLineStack(line):
    stack = []

    for chunk in line:
        if chunk in pairs:
            stack.append(chunk)

        else:
            if not stack:
                return []
            poppedChunk = stack.pop()
            if chunk != pairs[poppedChunk]:
                return []

    return stack


def completeScore(line):
    score = 0
    for chunk in line:
        score = score * 5
        score = score + completeScores[chunk]
    return score


def getLine(stack):
    return [pairs[chunk] for chunk in stack].reverse()


incompleteLinesStacks = [getIncompleteLineStack(incompleteLine) for incompleteLine in chunks if
                         getIncompleteLineStack(incompleteLine) != []]

scores = sorted([completeScore(getLine(stack)) for stack in incompleteLinesStacks])

print(scores[len(scores) // 2])
