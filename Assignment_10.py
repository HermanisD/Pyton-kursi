name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
handle = open(name)
counts=dict()
times=list()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From'): continue
    if len(line.split())<5: continue
   
    times.append(line.split()[5].split(":")[0])
  
for time in times:
    counts[time]=counts.get(time, 0)+1
counts=sorted(counts.items())

for key,val in counts:
    print(key, val)


