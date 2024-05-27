num = [int(input()) for _ in range(int(input()))]
result = {}

for i in num:
    if i not in result:
        result[i] = f(i)
        print(result[i])
    else:
        print(result[i])
