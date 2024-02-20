text = input()
replaceText = input()
r = int(input())

res = []
copyText=""

for i in range(r):
    a = input()
    copyText=text
    copyText=copyText.replace(replaceText,a)
    res.append(copyText)    

for r in res:
    print(r)