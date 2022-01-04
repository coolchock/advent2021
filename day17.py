xMin = 236
xMax = 262
yMin = -78
yMax = -58


def launch(xVelocity, yVelocity):
    x = 0
    y = 0
    maxY = 0

    for i in range(1000):
        x += xVelocity
        y += yVelocity
        maxY = max(maxY, y)

        if xVelocity < 0:
            xVelocity += 1
        elif xVelocity > 0:
            xVelocity -= 1

        yVelocity -= 1

        if (
                (x < xMin and xVelocity <= 0) or
                (x > xMax and xVelocity >= 0) or
                (y < yMin and yVelocity <= 0)
        ):
            return -99999999999999

        if xMin <= x <= xMax and yMin <= y <= yMax:
            return maxY

    return -99999999999999


# Part 1
maxY = -99999999999999
for yVelocity in range(-1000, 1000):
    for xVelocity in range(1000):
        y = launch(xVelocity, yVelocity)
        if y > maxY:
            maxY = y
            break
print(maxY)

# Part 2
count = 0
for yVelocity in range(-1000, 1000):
    for xVelocity in range(1000):
        i = launch(xVelocity, yVelocity)
        if i != -99999999999999:
            count += 1

print(count)
