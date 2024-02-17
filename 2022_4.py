a = int(input())
t1, w1, l1 = input().split()
t2, w2, l2 = input().split()

w1 = int(w1)
l2 = int(l2)

magicNumber = a +1 - w1 - l2

print(t1 + " must win ", str(magicNumber) + " matches", sep="")