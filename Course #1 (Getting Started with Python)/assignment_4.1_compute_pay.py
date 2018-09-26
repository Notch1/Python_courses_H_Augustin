def computepay(h,r):
    if h <= 40:
        pay = (h * r)
        return(pay)
    if h > 40:
        pay = (40 * r) + 1.5*r*(h - 40)
        return(pay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
print(p)