from functools import reduce

input = open('input.txt', 'r')
lines = input.read()

message = ''
for line in lines:
    message += format(int(line, 16), '04b')

message
versionNumbers = []
operators = {
    0: sum,
    1: lambda iter: reduce(lambda x, y: x * y, iter),
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}


def getLiteral(packet, i):
    j = i
    res = []
    while True:
        res.append(packet[j + 1: j + 5])
        if packet[j] == '0':
            return j + 5, int(''.join(res), 2)
        j += 5


def getPacket(packet, i):
    version, type = int(packet[i: i + 3], 2), int(packet[i + 3: i + 6], 2)
    versionNumbers.append(version)
    if type == 4:
        j, value = getLiteral(packet, i + 6)
        return j, value

    values = []
    lengthType = packet[i + 6]
    if lengthType == '0':
        length = int(packet[i + 7: i + 22], 2)
        j = i + 22
        while j < i + 22 + length:
            j, value = getPacket(packet, j)
            values.append(value)
    else:
        packets = int(packet[i + 7: i + 18], 2)
        j = i + 18
        for _ in range(packets):
            j, value = getPacket(packet, j)
            values.append(value)

    return j, operators[type](values)


# Part 1
getPacket(message, 0)
print(sum(versionNumbers))

# Part 2
print(getPacket(message, 0)[1])
