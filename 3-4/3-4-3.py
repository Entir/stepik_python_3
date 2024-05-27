words = []

with open('tmp_2.txt') as inf:
    for line in inf:
        words += line.strip().lower().split()
n = 0
w = []

for word in set(words):
    count = words.count(word)
    if count >= n:
        if count > n:
            w = []
        n = count
        w.append(word)

print(min(w), n)