# Filename: guessnum.py
# Author: Steve Berryman
# Description: This is a guessing game in which users are prompted to choose a number of games to be played,
#               and for each game played, a user will guess a number between 1 and 25, inclusive, which has 
#               been psuedo-randomly selected by the computer agent.

from random import randint

# game function
def play_game(num):
    num_guesses = 0     # count of number of guesses
    player_num = -1     # player's chosen number
    
    while player_num != num:
        player_num = int(input('Select a number from 1-25: '))
        num_guesses += 1
        if player_num > num:
            print('The number is lower')
        elif player_num < num:
            print('The number is higher')
        else:
            print('That\'s correct! It took you {} guesses'.format(num_guesses))
            
# main code
num_games = int(input('How many games would you like to play? '))   # number of games to be played  

# generate the number of games entered by the user
for game in range(num_games):
    num = randint(1, 26)    # pseudo-randomly chosen number
    play_game(num)
