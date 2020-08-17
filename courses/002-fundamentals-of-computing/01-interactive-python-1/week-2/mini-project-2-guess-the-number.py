# http://www.codeskulptor.org/#user47_lScmXBUIog_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
from math import log, ceil


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global player_guess, secret_number, upper_range, guess_count
    
    guess_count = int(ceil(log(upper_range, 2)))
        
    print "Welcome to Guess the Number, to begin, enter a number between 0 and " + str(upper_range)
    print str(guess_count) + " guesses remaining"
    secret_number = random.randrange(0, upper_range - 1)
    
# define event handlers for control panel
def range100():
    global upper_range
    upper_range = 100
    new_game()

def range1000():
    global upper_range
    upper_range = 1000
    new_game()
    # 10 guesses
    
def input_guess(guess):
    global guess_count
    try:
        player_guess = int(guess)
    except ValueError:
        print "Guess must be a number!"
        return
    
    if player_guess > upper_range:
        print "Guess should be between 0 and " + str(upper_range) + " inclusive"
        return
    
    print "Guess was " + guess
    
    if player_guess < secret_number:
        print "Higher"
    elif player_guess > secret_number:
        print "Lower"
    else:
        print "Correct!!"
        new_game()
        return
    
    # decrement our global guess count
    guess_count -= 1
    print str(guess_count) + " guesses left"
    
    if guess_count == 0:
        print "Game over! The secret number was " + str(secret_number) + ". Starting new game..."
        new_game()
        
# create frame
f = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
f.add_button("New Game", new_game)
f.add_button("Range is [0, 100)", range100)
f.add_button("Range is [0, 1000)", range1000)
f.add_input("Enter a guess", input_guess, 100)

f.start()

# init first name
range100()


# always remember to check your completed program against the grading rubric
