lst = [int(i) for i in input().split()]
x = int(input())
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        count += 1
if count == 0:
    print('Отсутствует')

