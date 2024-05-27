d = {}
txt = input().lower().split()

for i in txt:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in d:
    print(i, d[i])
