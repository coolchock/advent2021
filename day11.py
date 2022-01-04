input = open("input.txt", "r")

matrix = [[int(j) for j in i] for i in input.read().split('\n')]

rows = len(matrix)
columns = len(matrix[0])
flashes = 0


def isValid(i, j):
    return 0 <= i < rows and 0 <= j < columns


def flash(i, j):
    if matrix[i][j] == -1:
        return 0
    elif matrix[i][j] >= 9:
        flashes = 1
        matrix[i][j] = -1
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                newR = i + r
                newC = j + c
                if isValid(newR, newC):
                    flashes += flash(newR, newC)
        return flashes

    else:
        matrix[i][j] += 1
        return 0


step = 0
while True:
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == -1:
                continue
            if matrix[i][j] < 9:
                matrix[i][j] += 1
            else:
                flashes += flash(i, j)
    # Part 1
    if step == 99:
        print(flashes)
    sum = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
            sum += matrix[i][j]
    if sum == 0:
        # Part 2
        print(step)
        break
    step += 1
