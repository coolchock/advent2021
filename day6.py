from collections import Counter

input = open('input.txt', 'r')
lines = input.read().splitlines()
print(lines)

fishes = list(map(int, lines[0].split(",")))
fishes1 = fishes.copy()
fishes2 = fishes.copy()


def reproduce(days, fishes):
    for i in range(days):
        for j in range(len(fishes)):
            if fishes[j] > 0:
                fishes[j] -= 1
            else:
                fishes[j] = 6
                fishes.append(8)
    return len(fishes)


def reproduceOptimised(days, fishes):
    fishes = Counter(fishes)
    fishes[7] = 0
    fishes[8] = 0
    fishes[0] = 0

    for fish in fishes:
        if fish > 0:
            fishes[fish - 1] = fishes[fish]
            fishes[fish] = 0

        else:
            fishes[6] += fishes[0]
            fishes[8] += fishes[0]
            fishes[0] = 0

    return sum(fishes.values())


# Part 1
result = reproduce(80, fishes1)
print(result)

# Part 2
result = reproduceOptimised(256, fishes2)
fishes = Counter(fishes)
print(fishes)
