lot,dia = input().split()

div = int(lot) / int(dia)

removeUnity = div - int(div) # eliminem unitats
primerDecimal = int(removeUnity * 10) # trobem el 1r decimal
noFirstDecimal = removeUnity * 10 - int(removeUnity * 10)
segonDecimal = int(noFirstDecimal * 10) # trobem el 2n decimal

if (primerDecimal != 0) & (segonDecimal == 0):
    print(1)
else:
    print(0)