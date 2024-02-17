s = input()
res = ""

for i in s:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        res = res + '*'
    else:
        res +=i;

print(res)