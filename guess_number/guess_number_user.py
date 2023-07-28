import random
list_random_number = list(range(1, 101))
t = 10
# guess part
print('╻----------------╻ \n║GUESS THE NUMBER║ \n╹----------------╹ \n TYPE ANY NUMBER \n  BETWEEN 1-100')
random_number = random.choice(list_random_number)
while True:
    # check int part
    while True:
        try:
            print('\n[You have', t, 'chance(s) remaining]')
            guess_number = int(input('\n> '))
            break
        except TypeError:
            print('It is not a number')
    # more or less part + win or lose part
    if random_number == guess_number:
        print('╻----------------╻ \n║    YOU  WON!   ║ \n╹----------------╹')
        break
    elif t == 1:
        print('╻----------------╻ \n║   GAME  OVER!  ║ \n╹----------------╹')
        break
    if random_number > guess_number:
        print('MORE...')
    else:
        print('LESS...')
    t -= 1
print(' SECRET NUMBER', random_number)
