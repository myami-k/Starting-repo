import random


def is_correct(guess, any_range, score_1, score_2):
    if guess == any_range:
        score_1 += 1
    elif guess in all_ranges:
        score_2 += 1
    return score_1, score_2


colors = ["R", "Y", "B", "G", "O", "P"]
range_no1 = random.choice(colors)
range_no2 = random.choice(colors)
range_no3 = random.choice(colors)
range_no4 = random.choice(colors)
all_ranges = [range_no1, range_no2, range_no3, range_no4]

chances = 6

while True:

    if chances > 1:
                print("CHANCE(S) REMAINING:", chances)

    guess_input = input('\n  > ')
    if any(box in guess_input for box in colors):
        if len(guess_input) == 4:

            guesses = list(guess_input)
            correct, almost = 0, 0
            length = len(guesses)
            for i in range(length):
                if i == 0:
                    correct, almost = is_correct(guesses[i], range_no1, correct, almost)
                if i == 1:
                    correct, almost = is_correct(guesses[i], range_no2, correct, almost)
                if i == 2:
                    correct, almost = is_correct(guesses[i], range_no3, correct, almost)
                if i == 3:
                    correct, almost = is_correct(guesses[i], range_no4, correct, almost)

            chances -= 1

            print(guesses, " CORRECT:", correct, " ALMOST:", almost)

            if correct == 4:
                print("YOU WON")
                print("THE CODE WAS:", all_ranges)
                exit()
            if chances == 0:
                print("YOU LOST")
                print("THE CODE WAS:", all_ranges)
                exit()

        else:
            print('INVALID 2')
    else:
        print('INVALID 1')
