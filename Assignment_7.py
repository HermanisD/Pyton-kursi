# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lh=line.upper()
    print(lh.strip())