# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# load modules
import random


#### helper functions ####

# convert name to number
def name_to_number(name):
    """
    Function to convert name to a number 
    """
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
        print "Error: Not a valid choice"
    
    # convert name to number using if/elif/else
    # don't forget to return the result!


# convert input number to RPSLS
def number_to_name(number):
    """
    Function to convert number thrown to RPSLS choice
    """
    
    if number == 0 :
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
        print "Error: Not a valid number"
            
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
#### creation of rpsls program ####


def rpsls(player_choice): 
    """
    Use helper functions to create RPSLS. Winner based on
    modular arithmetic, where difference between assigned numbers 
    modulo 5 determines winner: 0 is a tie; 1 or 2, computer wins;
    3 or 4, player wins.
    """
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice + "."
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # print and convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses " + number_to_name(comp_number) + "."
    
    # compute difference of comp_number and player_number modulo five    
    decision = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if decision == 0:
        print "It's a tie!"
    elif decision <= 2:
        print "Computer wins!"
    else:
        print "Player wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


