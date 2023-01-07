# Rock Paper Scissor game

import random
lives = 3

def play():
    player = input("Choose 'r' for rock, 'p' for paper, 's' for scissor or 'q' to quit: ")
    choices = ['r', 'p', 's', 'q']
    global lives

    if player in choices:
        if player == 'q':
            exit()

        computer = random.choice(['r', 'p', 's'])
        print(f'Computer chose {computer}')

        if player == computer:
            return f"It's a TIE! You still have {lives} lives"

        if is_win(player, computer):
            lives += 1
            print('You WON! +1 life')
            return f'You now have {lives} lives'

        lives -= 1
        print('You LOST! -1 life')
        return f'You now have {lives} lives'

    else:
        print('Invalid input. Please enter a valid value')
        return play()

def is_win(user, opponent):
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
        return True

while lives > 0:
    print(play())
else:
    print('You have 0 lives left. GAME OVER')