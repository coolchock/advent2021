from collections import defaultdict

input = open('input.txt', 'r')
lines = input.read()

nodes = defaultdict(list)
for line in lines.split("\n"):
    node1, node2 = line.split('-')
    nodes[node1].append(node2)
    nodes[node2].append(node1)


def visit(node, visited, two=False):
    if node == 'start' and visited:
        return 0
    if node == 'end':
        return 1
    if node.islower() and node in visited:
        if two:
            two = False
        else:
            return 0
    visited = visited | {node}
    res = 0
    for nextNode in nodes[node]:
        res += visit(nextNode, visited, two)
    return res


# Part 1
print(visit('start', set()))
# Part 2
print(visit('start', set(), True))
