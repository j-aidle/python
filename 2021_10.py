a = int(input())
players = dict()

for i in range(a):
    words = input().split()
    name = words[0]
    goals = int(words[2])
    spades = int(words[6])
    players[name] = goals*4 + spades*2
    
bests = [ k for k,v in players.items() if v == max(players.values())]

if len(bests) == 1:
    mvp = bests[0]
    print(mvp + ' is the MVP with ' + str(players[mvp]) + ' points!')
else:
    print('DRAW')
