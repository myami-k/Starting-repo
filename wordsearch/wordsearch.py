

def main_function():
    file_words_input = str(input("The file containing the words: "))
    dictionary_words = words_function(file_words_input)
    file_puzzle_input = str(input("The file containing the puzzle: "))
    puzzle_function(file_puzzle_input)
    direction_input = str(input("The direction you'll be looking for: "))
    direction_function(direction_input, dictionary_words, file_puzzle_input)


def words_function(prompt):
    while True:
        try:
            fp_words = open(prompt).read().splitlines()
            break
        except FileNotFoundError:
            print('Invalid words file')
            exit()
    dictionary_words = {}
    for lines in fp_words:
        key, value = lines.split(":")
        dictionary_words[key] = value
    for key, value in dictionary_words.items():
        print(f'{key}:{value}')
    return dictionary_words


def puzzle_function(prompt):
    while True:
        try:
            fp_puzzle = open(prompt).read()
            break
        except FileNotFoundError:
            print('Invalid puzzle file')
            exit()
    print(fp_puzzle)


def direction_function(prompt, dictionary, puzzle_path):
    list_puzzle = open(puzzle_path).read().splitlines()
    while True:
        if prompt == "h":
            horizontal_function(list_puzzle, dictionary)
        elif prompt == "v":
            vertical_function(list_puzzle, dictionary)
        else:
            print('Invalid direction')
        break


def horizontal_function(list_puzzle, dictionary):
    row_pos = 0
    for row in list_puzzle:
        row_list = list(row.replace(" ", "").lower())
        length = len(row_list)
        col_pos = 1
        row_pos += 1
        for start in range(length):
            finder = ""
            for letters in row_list:
                finder += letters
                if finder in dictionary:
                    print(f'{finder} found at [{row_pos}, {col_pos}]')
            row_list.pop(0)
            col_pos += 1


def vertical_function(list_puzzle, dictionary):
    scale = 0
    col_pos = 0
    length = len(list_puzzle)
    for times in range(length):
        col_list = []
        for col in list_puzzle:
            row_list = list(col.replace(" ", "").lower())
            col_list.append(row_list[scale])
        row_pos = 1
        col_pos += 1
        for start in range(length):
            finder = ""
            for letters in col_list:
                finder += letters
                if finder in dictionary:
                    print(f'{finder} found at [{row_pos}, {col_pos}]')
            col_list.pop(0)
            row_pos += 1
        scale += 1


main_function()
