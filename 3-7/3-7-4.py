cord = [0, 0]

for i in range(int(input())):
    x = input().split()

    if x[0] == 'север':
        cord[1] += int(x[1])

    elif x[0] == 'запад':
        cord[0] -= int(x[1])

    elif x[0] == 'юг':
        cord[1] -= int(x[1])

    elif x[0] == 'восток':
        cord[0] += int(x[1])

print(*cord)
