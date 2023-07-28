import random


def rps(pc_choice, user_choice):
    global user_score, pc_score
    if user_choice == 'ROCK':
        if pc_choice == 'SCISSORS':
            user_score += 1
        elif pc_choice == 'PAPER':
            pc_score += 1
    elif user_choice == 'PAPER':
        if pc_choice == 'ROCK':
            user_score += 1
        elif pc_choice == 'SCISSORS':
            pc_score += 1
    elif user_choice == 'SCISSORS':
        if pc_choice == 'PAPER':
            user_score += 1
        elif pc_choice == 'ROCK':
            pc_score += 1


pc_score = 0
user_score = 0
while True:
    user = str(input('\n> '))
    if user in ("ROCK", "PAPER", "SCISSORS"):
        list_rps = ["ROCK", "PAPER", "SCISSORS"]
        pc = random.choice(list_rps)
        rps(pc, user)
        print('\n', user, ' VS ', pc, '\n   ', user_score, " -- ", pc_score)
        if pc_score == 3:
            print('\n   YOU LOST')
            exit()
        elif user_score == 3:
            print('\n   YOU WON')
            exit()
    else:
        print('\n   INVALID')
