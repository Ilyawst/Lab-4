x = 0
y = 0

while True:
    dir = input('Enter direction: ')
    if dir == 'Treasure!':
        break
    direction, steps = dir.split()
    steps = int(steps)

    if direction == 'North':
        y += steps
    elif direction == 'South':
        y -= steps
    elif direction == 'East':
        x += steps
    elif direction == 'West':
        x -= steps

print(x, y)
