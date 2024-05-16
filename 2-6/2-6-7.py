a = []

while True:
    num = int(input())
    a.append(num)
    if sum(a) == 0:
        break

print(sum([i*i for i in a]))

