a = int(input())
text=""


if a == 0:
    print("-")
else:
    for i in range(a):
        text+="*"
print(text)