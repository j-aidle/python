acrosticText =""
celestinaText =""

print("Output for acrostic.txt")
#obrim i llegim el contingut
with open("acrostic.txt", "r") as acrostic:
    #per cada linea copiem la primera paraula al text
    for line in acrostic:
        acrosticText += line[0]
print(acrosticText)
print()
print("Output for celestina.txt")
with open("celestina.txt", "r") as celestina:
    for line in celestina:
        celestinaText += line[0]
print(celestinaText)