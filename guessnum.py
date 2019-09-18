from random import randint

def play_game(num):
    num_guesses = 0
    player_num = -1
    
    while player_num != num:
        player_num = int(input('Select a number from 1-25: '))
        num_guesses += 1
        if player_num > num:
            print('The number is lower')
        elif player_num < num:
            print('The number is higher')
        else:
            print('That\'s correct! It took you {} guesses'.format(num_guesses))

num_games = int(input('How many games would you like to play? '))

for game in range(num_games):
    num = randint(1, 26)
    play_game(num)
