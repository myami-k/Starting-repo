import random
less_n, more_n = 101, 1
print('╻-------------------╻ \n║FINDING YOUR NUMBER║ \n╹-------------------╹')
while True:
    pc_guess = random.choice(list(range(more_n, less_n)))
    print('\n╻---------- \n║  ', pc_guess, '?   \n╹----------')
    user_ans = str(input('> '))
    if user_ans == "CORRECT":
        exit()
    else:
        if user_ans == "LESS":
            less_n = pc_guess
        elif user_ans == "MORE":
            more_n = pc_guess + 1
        else:
            print('TYPE MORE OR LESS')
