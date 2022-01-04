from itertools import permutations

input = open('input.txt', 'r')
lines = input.read()

pairs = [eval(line) for line in lines.split('\n')]


def addL(x, y):
    if not y:
        return x
    if type(x) == int:
        return x + y
    return [addL(x[0], y), x[1]]


def addR(x, y):
    if not y:
        return x
    if type(x) == int:
        return x + y
    return [x[0], addR(x[1], y)]


def explode(x, layer):
    if type(x) == int:
        return False, x, 0, 0
    left, right = x
    if layer == 4:
        return True, 0, left, right
    exploded, next, l, r = explode(left, layer + 1)
    if exploded:
        return True, [next, addL(right, r)], l, 0
    exploded, next, l, r = explode(right, layer + 1)
    if exploded:
        return True, [addR(left, l), next], 0, r
    return False, x, 0, 0


def split(number):
    if type(number) == int:
        if number > 9:
            return [number // 2, number // 2 + (number & 1)]
        return number
    l, r = number
    left = split(l)
    if left != l:
        return [left, r]
    return [l, split(r)]


def snails(x, y):
    result = [x, y]
    while True:
        exploded, result, i, j = explode(result, 0)
        if not exploded:
            previous = result
            result = split(result)
            if result == previous:
                return result


def magnitude(x):
    if type(x) == int:
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


# Part 1
current = pairs[0]
for line in pairs[1:]:
    current = snails(current, line)
print(magnitude(current))

# Part 2
result = 0
for x, y in permutations(pairs, 2):
    cur = snails(x, y)
    result = max(result, magnitude(current))
print(result)
