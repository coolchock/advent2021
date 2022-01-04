input = open('input.txt', 'r')

lines = input.read().splitlines()

# Part 1
epsilon = ""
gamma = ""

for column in zip(*lines):
    if column.count('0') > column.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(epsilon * gamma)

# Part 2

# ox
lines = lines[::]
for i in range(len(lines[0])):
    bits = list(zip(*lines))[i]
    if len(lines) == 1:
        break
    if bits.count('0') > bits.count('1'):
        lines = [line for line in lines if line[i] == '0']
    else:
        lines = [line for line in lines if line[i] == '1']
if len(lines) == 1:
    oxygen = lines[0]
oxygen = int(oxygen, 2)

# co2:
lines = lines[::]
for i in range(len(lines[0])):
    bits = list(zip(*lines))[i]
    if len(lines) == 1:
        break
    if bits.count('0') <= bits.count('1'):
        lines = [line for line in lines if line[i] == '0']
    else:
        lines = [line for line in lines if line[i] == '1']
if len(lines) == 1:
    co2 = lines[0]
co2 = int(co2, 2)
print(co2 * oxygen)
