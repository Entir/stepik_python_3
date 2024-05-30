import requests

adr_x = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('test_2.txt', 'r', encoding='utf-8') as file:
    adr = file.readline().strip()

r = requests.get(adr)

while True:
    if not r.text.startswith('We'):
        r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + r.text)
        continue
    else:
        print(r.text)
    break

