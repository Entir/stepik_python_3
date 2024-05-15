num = [int(i) for i in input().split()]

for i in range(len(num)):
    if len(num) == 1:
        print(num[0])
        break

    if i == 0:
        print(num[i + 1] + num[len(num) - 1], end=' ')
        continue

    if i == len(num) - 1:
        print(num[0] + num[i - 1], end=' ')
        break

    print(num[i - 1] + num[i + 1], end=' ')
