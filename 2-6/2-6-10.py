a = []

while True:
    tmp = input()
    if tmp == 'end':
        break
    else:
        a.append([int(i) for i in tmp.split()])


result = a.copy()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i - 1][j] + a[(i + 1) % len(a)][j] + a[i][j - 1] + a[i][(j + 1) % len(a[i])], end=' ')
    print()

