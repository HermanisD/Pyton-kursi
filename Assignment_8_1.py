fname = input("Enter file name: ")
fh = open(fname)
lst = list()
wrds = list()
for line in fh:
    lst = lst + line.rstrip().split()

for word in lst:
    if word in wrds:

        continue
    else:

        wrds.append(word)
wrds.sort()
print(wrds)
