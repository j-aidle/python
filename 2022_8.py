count1 = 0
count2 = 0
t1, t2 = input().split(" - ")

for i in range(3):
    r1,r2 = input().split(" - ")
    if (int(r1) > int(r2)):
        count1 +=1
    elif (int(r1) < int(r2)):
        count2 +=1 
    if (count1 == 2):
        print(t1, "won the match", count1, "-", count2, ".")
        break
    if (count2 == 2):
        print(t2, "won the match", count1, "-", count2, ".")        
        break