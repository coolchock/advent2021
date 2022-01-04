input = open('input.txt', 'r')

commands = [command.split(' ') for command in input.read().splitlines()]

# Part 1
horizontal = 0
depth = 0

for direction, value in commands:
    if direction == 'forward':
        horizontal += int(value)
    elif direction == 'down':
        depth += int(value)
    else:
        depth -= int(value)

print(horizontal * depth)

# Part 2
aim = 0
horizontal = 0
depth = 0

for direction, value in commands:
    if direction == 'forward':
        horizontal += int(value)
        depth += aim * int(value)
    elif direction == 'down':
        aim += int(value)
    else:
        aim -= int(value)

print(horizontal * depth)
