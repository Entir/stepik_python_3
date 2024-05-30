n = int(input())
matrix = []
for _ in range(n):
    tmp = [0 for e in range(n)]
    matrix.append(tmp)
x, y, = 0, 0
d_x, d_y = 0, 1
matrix[0][0] = 1
count = 2

while count <= n * n:
    if (0 <= x + d_x <= n - 1) and (0 <= y + d_y <= n - 1) and (matrix[x + d_x][y + d_y] == 0):
        matrix[x + d_x][y + d_y] = count
        count += 1
        x += d_x
        y += d_y
    else:
        if d_y == 1:
            d_y = 0
            d_x = 1
        elif d_x == 1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x = 0
            d_y = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

