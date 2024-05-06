num = int(input())

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
num = num // 10
f = num % 10

if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
