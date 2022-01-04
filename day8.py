input = open('input.txt', 'r')

# Part 1
count = 0
for line in input:
    signal, output = line.strip().split(' | ')
    numberLengths = [len(number) for number in output.split()]
    for length in numberLengths:
        if length in [2, 3, 4, 7]:
            count += 1
print(count)
input.close()

# Part 2
input = open('input.txt', 'r')
sum = 0
for line in input:
    signal, output = line.strip().split(' | ')
    signal = signal.split()
    output = output.split()

    numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

    five = []
    six = []

    for number in signal:
        length = len(number)
        if length == 2:
            numbers[1] = set(number)
        if length == 3:
            numbers[7] = set(number)
        if length == 4:
            numbers[4] = set(number)
        if length == 5:
            five.append(set(number))
        if length == 6:
            six.append(set(number))
        if length == 7:
            numbers[8] = set(number)

    for number in six:
        if numbers[4].issubset(set(number)):
            numbers[9] = set(number)
        else:
            if numbers[7].issubset(set(number)):
                numbers[0] = set(number)
            else:
                numbers[6] = set(number)

    for number in five:
        if numbers[7].issubset(set(number)):
            numbers[3] = set(number)
        else:
            if len(set(number).intersection(numbers[4])) == 3:
                numbers[5] = set(number)
            else:
                numbers[2] = set(number)

    digits = ''
    for number in output:
        s = set(number)
        for i, key in enumerate(numbers.values()):
            if s == key:
                digits = digits + str(i)
    sum += int(digits)
print(sum)
