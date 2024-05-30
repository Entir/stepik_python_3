import requests

with open('test_1.txt', 'r', encoding='utf-8') as file:
    adr = file.readline().strip()

r = requests.get(adr)

print( len(r.text.splitlines()))

