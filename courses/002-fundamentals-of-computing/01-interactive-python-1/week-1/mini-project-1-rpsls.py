# http://www.codeskulptor.org/#user47_uLGNq6gQMG_0.py

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """Returns number representation of a choice for a given name"""
    if name == "rock":
        return 0   
    elif name == "Spock":
        return 1   
    elif name == "paper":
        return 2   
    elif name == "lizard":
        return 3   
    elif name == "scissors":
      return 4
    else:
        # Not a valid choice
        print "Error: Invalid name!"
        return None

def number_to_name(number):
    """Returns the name representation of a choice for a given number"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        # Not a valid choice
        print "Error: Invalid number!"
        return None    

def rpsls(player_choice): 
    print
    # print out the message for the player's choice
    print "Player choses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer choses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    dif = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if dif == 1 or dif == 2:
        print "Computer Wins!"
    elif dif == 3 or dif == 4:
        print "Player Wins"
    else:
        print "Player and computer tie!"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


