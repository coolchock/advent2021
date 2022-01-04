import re as regex
from collections import Counter

file = open('input.txt', 'r')
lines = file.read()

template = lines.split('\n')[0]
insertions = dict(regex.findall(r'(.+) -> (.+)', lines))


def step(count):
    counter = Counter()
    for k in count:
        counter[k[0] + insertions[k]] += count[k]
        counter[insertions[k] + k[1]] += count[k]
    return counter


def insert(n):
    counter = Counter()
    for i in range(len(template) - 1):
        counter[template[i:i + 2]] += 1

    for j in range(n):
        nxt = step(counter)
        counter = nxt

    result = Counter()
    for k in counter:
        result[k[0]] += counter[k]
    result[template[-1]] += 1

    return max(result.values()) - min(result.values())


# Part 1
print(insert(10))
# Part 2
print(insert(40))
