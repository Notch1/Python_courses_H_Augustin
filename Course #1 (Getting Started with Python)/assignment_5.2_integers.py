# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
# other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown. 


largest = None
smallest = None

while True:
    bum = input("Enter a number: ")
    if bum == "done" :
        break
    try:
        rum = int(bum)
    except:
        print("Invalid input")
        continue
    
    if largest is None:
        largest = rum
    elif largest < rum:
        largest = rum
        
    if smallest is None:
        smallest = rum
    elif smallest > rum:
        smallest = rum  
    
    
print ("Maximum is ", largest)
print ("Minimum is ", smallest)