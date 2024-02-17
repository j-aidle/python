ranks = ["Admiral", "Captain", "Commander", "Lieutenant", "Officer"]

a = input()

if a == "S":
    n1 = input()
    r1 = input()
    n2 = input()
    r2 = input()    
    m = input()
    t = int(input())
    if (ranks.index(r1)<ranks.index(r2)):
        print('URGENT,',n1,',',r1,',',n2,',',r2,',',m,',',t, sep="")
    else:
        print(n1,',',r1,',',n2,',',r2,',',m,',',t, sep="")       

elif a == "R":
    n1,r1,n2,r2,m,t = input().split(",")
    if (ranks.index(r1)<ranks.index(r2)):
        print('<<< URGENT >>>')
        print("From: " + n1)
        print("From rank: " + r1)
        print("To: " + n2)
        print("To rank: " + r2)
        print("Content: " + m)
        print("Timestamp: " + t)
    else:
        print("From: " + n1)
        print("From rank: " + r1)
        print("To: " + n2)
        print("To rank: " + r2)
        print("Content: " + m)
        print("Timestamp: " + t)
else:
    print("Invalid input.")