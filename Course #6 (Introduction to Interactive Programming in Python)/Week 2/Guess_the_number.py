# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code here
num_range = 100
attempts = 0

# helper function to start and restart the game
def new_game():
    global secret_number, attempts
    attempts = int(math.ceil(math.log(num_range, 2)))
    secret_number = random.randrange(0, num_range)
    print "New game."
    print "Range is from 0 to " + str(num_range) + "."
    print "Please enter your number."
    print "Number of remaining guesses:", attempts
    print""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global num_range, attempts
    the_num = int(guess)
    attempts -= 1 
    print "You guessed " + str(the_num) + '.' 
    
    if the_num < 0 or the_num >= num_range:
        print "Please enter number between 0 and", num_range - 1
        print "Remaining guesses: ", attempts
        print ""
        return 
    
    if the_num > secret_number:
        print "Lower."
        print "Remaining guesses: ", attempts
        print ""
        
    elif the_num < secret_number:     
        print "Higher."
        print "Remaining guesses: ", attempts
        print ""
        
    else:
        print "You got it!"
        print ""
        new_game()
        
    if (attempts == 0):
        print "Sorry, you ran out of attempts. \nThe number was " + str(secret_number) + ". Game over."        
        print""
        new_game()


# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [1, 100)", range100, 150)
f.add_button("Range is [1, 1000)", range1000, 150)
f.add_input("Enter a guess", input_guess, 75)             
# call new_game 
new_game()