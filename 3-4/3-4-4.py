data = []

with open('tmp_3.txt') as inf:
    for line in inf:
        data.append(line.strip().split(';'))

z = len(data)

with open('tmp_3-1.txt', 'w', encoding='utf-8') as inf:

    a = 0
    b = 0
    c = 0

    for i in data:
        inf.write(str(sum([int(x) for x in i[1:]]) / 3) + '\n')
        a += int(i[1])
        b += int(i[2])
        c += int(i[3])

    inf.write(str(a / z) + ' ' + str(b / z) + ' ' + str(c / z) + '\n')

