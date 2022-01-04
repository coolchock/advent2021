input = open('input.txt', 'r')
numbers = [int(number) for number in input]

# Part 1
counter = 0
for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        counter += 1

print(counter)

counter = 0

# Part 2
for i in range(len(numbers) - 3):
    sum1 = numbers[i] + numbers[i + 1] + numbers[i + 2]
    sum2 = numbers[i + 1] + numbers[i + 2] + numbers[i + 3]
    if sum1 < sum2:
        counter += 1

print(counter)
