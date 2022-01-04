input = open('input.txt', 'r')
lines = input.read()

numbers, *boards = lines.split('\n\n')
numbers = list(map(int, numbers.split(',')))
boards = [[list(map(int, row.split())) for row in board.split('\n')] for board in boards]


def checkRows(board):
    return any(all(x == 'X' for x in row) for row in board)


def isWinning(board):
    transpose = list(map(list, zip(*board)))
    return checkRows(board) or checkRows(transpose)


def checkBoardNumber(board, x):
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == x:
                board[i][j] = 'X'
    return board


def sumBoard(board):
    return sum(sum(number for number in row if type(number) == int) for row in board)


def partOne():
    for number in numbers:
        for i, board in enumerate(boards):
            current = checkBoardNumber(board, number)
            if isWinning(current):
                return sumBoard(current) * number
            boards[i] = current


def partTwo():
    winners = set()
    for number in numbers:
        for i, board in enumerate(boards):
            if i in winners:
                continue
            current = checkBoardNumber(board, number)
            if isWinning(current):
                if len(winners) == len(boards) - 1:
                    return sumBoard(current) * number
                winners.add(i)
            boards[i] = current


print(partOne())
print(partTwo())
