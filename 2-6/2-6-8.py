num = int(input())
result = []

for i in range(num):
    result += [i] * i

if num == 1:
    print(1)
else:
    print(*result[:num])
