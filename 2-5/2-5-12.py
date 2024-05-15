num = sorted([int(i) for i in input().split()])
result = []
for i in num:
    if num.count(i) > 1 and i not in result:
        result.append(i)

print(*result)

