score = input("Enter Score: ")
if float(score) > 1 or float(score) < 0:
    print ("error")
elif float(score) >= 0.9:
    print ("A")
elif float(score) >= 0.8:
    print ("B")
elif float(score) >= 0.7:
    print ("C")
elif float(score) >= 0.6:
    print ("D")
elif float(score) < 0.6:
    print ("F")
 

