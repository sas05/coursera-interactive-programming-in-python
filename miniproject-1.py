# Rock-paper-scissors-lizard-Spock template

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
    # convert name to number using if/elif/else
    # don't forget to return the result!
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
       return "non matched";


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!

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
       return "non matched";


def rpsls(name):

    # print a blank line to separate consecutive games
    print " "

    # print out the message for the player's choice
    print "player's chooses " + name

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(5)

    # convert comp_number to comp_choice using the function number_to_name()
    computer_name = number_to_name(computer_number)

    # print out the message for computer's choice
    print "Computer chooses " + computer_name

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - computer_number) % 5

    # use if/elif/else to determine winner, print winner message
    if difference in [1, 2]:
        result = "Player wins!"
    elif difference == 0:
        result = "Player and computer tie!"
    else:
        result = "Computer wins!"

    print result


# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric