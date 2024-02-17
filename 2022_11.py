hours = [h.strip() for h in input().split(sep=',')][:8]

min = []

for h in hours:
    calc = h.split(':')
    min.append(int(calc[0])*60+int(calc[1]))

t = min[0]
  
for i in range(1,len(min)):
    t -= min[i]

if t >=0:
    print(f"{t // 60:02d}:{t % 60:02d} hours of viewing remaining.")
else:
    print(f"LIMIT EXCEEDED BY {-t // 60:02d}:{-t % 60:02d}. Benigno punished!")