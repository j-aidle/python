gender = input()
rbc = float(input())
wbc = int(input())
pla = int(input())
hmg = float(input())
hmt = int(input())

if (gender == 'Male'):
    if rbc >= 4.3 and rbc <=5.9:
        print ('Red blood cells: NORMAL')
    if rbc < 4.3 or rbc >5.9:
        print('Red blood cells: VISIT THE DOCTOR')
    if wbc >= 4500 and wbc <=11000:
        print ('White blood cells: NORMAL')
    if wbc < 4500 or wbc >11000:
        print('White blood cells: VISIT THE DOCTOR')
    if pla >= 150000 and pla <=400000:
        print ('Platelets: NORMAL')
    if pla < 150000 or pla >400000:
        print('Platelets: VISIT THE DOCTOR')
    if hmg >= 13.5 and hmg <=17.5:
            print ('Hemoglobin: NORMAL')
    if hmg < 13.5 or hmg >17.5:
        print('Hemoglobin: VISIT THE DOCTOR')
    if hmt >= 41 and hmt <=53:
            print ('Hematocrit: NORMAL')
    if hmt < 41 or hmt >53:
        print('Hematocrit: VISIT THE DOCTOR')          
if (gender == 'Female'):
    if rbc >= 3.5 and rbc <=5.5:
        print ('Red blood cells: NORMAL')
    if rbc < 3.5 or rbc >5.5:
        print('Red blood cells: VISIT THE DOCTOR')
    if wbc >= 4500 and wbc <=11000:
        print ('White blood cells: NORMAL')
    if wbc < 4500 or wbc >11000:
        print('White blood cells: VISIT THE DOCTOR')
    if pla >= 150000 and pla <=400000:
        print ('Platelets: NORMAL')
    if pla < 150000 or pla >400000:
        print('Platelets: VISIT THE DOCTOR') 
    if hmg >= 12.0 and hmg <=16.0:
            print ('Hemoglobin: NORMAL')
    if hmg < 12.0 or hmg >16.0:
        print('Hemoglobin: VISIT THE DOCTOR')
    if hmt >= 36 and hmt <=46:
        print ('Hematocrit: NORMAL')
    if hmt < 36 or hmt >46:
        print('Hematocrit: VISIT THE DOCTOR')     