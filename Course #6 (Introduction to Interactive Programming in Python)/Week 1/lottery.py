# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    a = random.randrange(0,60) 
    b = random.randrange(0,60) 
    c = random.randrange(0,60) 
    d = random.randrange(0,60) 
    e = random.randrange(0,60) 
    z = random.randrange(0,36)

    print ("Today's numbers are " + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(d) + ", and " + str(e) + "." + 
           " The Powerball number is " + str(z) + ".")

   
powerball()

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
