# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x=0
s=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num=line.find(":")
    value=float(line[num+1:])
    x=x+1
    s=s+value
print("Average spam confidence: ", s/x)