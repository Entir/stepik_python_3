n = int(input())

if (n % 10 == 0) or (n % 10 >= 5) or (14 >= n % 100 >= 11):
    print(n, 'программистов')

elif n % 10 == 1:
    print(n, 'программист')

elif 4 >= n % 10 >= 2:
    print(n, 'программиста')

