input = open('input.txt')
enhancement, picture = input.read().split('\n\n')
picture = picture.splitlines()

pixels = set()
xMin, yMin, xMax, yMax = float('inf'), float('inf'), 0, 0
for x, row in enumerate(picture):
    for y, point in enumerate(row):
        if point == '#':
            pixels.add((x, y))
            xMin = min(xMin, x)
            yMin = min(yMin, y)
            xMax = max(xMax, x)
            yMax = max(yMax, y)

outer = '.'
for algorithmCall in range(50):
    xMin -= 1
    yMin -= 1
    xMax += 1
    yMax += 1
    newPixels = set(pixels)
    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            i = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    condition = not (xMin < x + dx < xMax) or not (yMin < y + dy < yMax)
                    i <<= 1
                    i |= (x + dx, y + dy) in pixels or (condition and outer == '#')
            if enhancement[i] == '#':
                newPixels.add((x, y))
            else:
                newPixels.discard((x, y))
    outer = enhancement[-1 if outer == '#' else 0]
    pixels = newPixels
    # Part 1
    if algorithmCall == 1:
        print(len(pixels))

# Part 2
print(len(pixels))
