score = input("Enter Score: ")
score = float(score)
if score<0.0:
    print("Error")
if score < 0.6:
    print("F")
elif score < 0.7:
    print("D")
elif score < 0.8:
    print ("C")
elif score < 0.9:
    print ("B")
elif score < 1.0:
    print ("A")
else:
    print("Error")
