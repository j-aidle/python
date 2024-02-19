w, h = input().split()
#passem els valors a integers
w = int(w)
h = int(h)

pixels = []
histogram = [0 for x in range(256)]

for i in range(h):
    row = [int(x) for x in input().split()]
    pixels.extend(row) #per afegir elements al vector de pixels
    for pixel_value in row:
        histogram[pixel_value] += 1

#mostrem el histogram en una matriu de 16x16
for j in range(16):
    for k in range(16):
        print(histogram[j * 16 + k], end=' ')
    print()
