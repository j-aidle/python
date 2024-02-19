res = []
text=""


while True:
    a = input()
    if "." in a:
        res.append(a)
        break
    res.append(a)

for r in res:
    for i in reversed(range(len(r))):
        if r[i] == 'A':
            text += 'T'
        if r[i] == 'T':
            text += 'A'
        if r[i] == 'C':
            text += 'G'
        if r[i] == 'G':
            text += 'C'
    text += "\n"
    print(r)

print(text)
