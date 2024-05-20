lst = []

while True:
    tmp = input()
    if tmp == 'end':
        break
    else:
        lst.append([int(i) for i in tmp.split()])

print(lst)

result = lst.copy()
print(result)

# дорешать когда-нибудь эту задачку и следующую, посмотрев видео....

# https://www.youtube.com/watch?v=0qtLrRm36J0&t=6s

