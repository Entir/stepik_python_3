count = []
commands = {}

for i in range(int(input())):
    tmp = input().split(';')
    count.append([tmp[0], int(tmp[1]), tmp[2], int(tmp[3])])

for i in count:
    if i[0] not in commands:
        commands[i[0]] = [0, 0, 0, 0, 0]
    if i[2] not in commands:
        commands[i[2]] = [0, 0, 0, 0, 0]

    # victory
    if i[1] > i[3]:
        commands[i[0]][0] += 1
        commands[i[0]][1] += 1
        commands[i[0]][4] += 3

        commands[i[2]][0] += 1
        commands[i[2]][3] += 1

    # loose
    elif i[1] < i[3]:
        commands[i[2]][0] += 1
        commands[i[2]][1] += 1
        commands[i[2]][4] += 3

        commands[i[0]][0] += 1
        commands[i[0]][3] += 1

    # nobody
    else:
        commands[i[0]][0] += 1
        commands[i[0]][2] += 1
        commands[i[0]][4] += 1

        commands[i[2]][0] += 1
        commands[i[2]][2] += 1
        commands[i[2]][4] += 1

for key, value in commands.items():
    print(str(key) + ':', *value)
