res = []
text=""

while True:
    a = input()
    if "." in a:
        res.append(a)
        break
    res.append(a)

for i in range(a):
    if a.charAt(i) == 'A':
        text += 'T'
    if a.charAt(i) == 'T':
        text += 'A'
    if a.charAt(i) == 'C':
        text += 'G'
    if a.charAt(i) == 'G':
        text += 'C'


for r in res:
    print(r)