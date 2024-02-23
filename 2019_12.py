res = []

while True:
    a = input()

    if a == "#":
        break

    t, e = a.split()
    text=""

    if t == "Ship":
        energy = float(e)/0.3
        ce = energy*23.3
        text = str(t) + " " + str(round(energy,1)) + " " + str(round(ce,1))
        res.append(text)
    if t == "Train":
        energy = float(e)/0.32
        ce = energy*23.1
        text = str(t) + " " + str(round(energy,1)) + " " + str(round(ce,1))
        res.append(text)
    if t == "Road":
        energy = float(e)/2.12
        ce = energy*160.1
        text = str(t) + " " + str(round(energy,1)) + " " + str(round(ce,1))
        res.append(text)
    if t == "Plane":
        energy = float(e)/21.01
        ce = energy*1577.1
        text = str(t) + " " + str(round(energy,1)) + " " + str(round(ce,1))
        res.append(text)


for r in res:
    print(r)