def computepay(h, r):
    if h<=40:
        return h*r
    else:
        return 40*r+(h-40)*r*1.5    

hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Rate: ")
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)