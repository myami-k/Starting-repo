import random


def choose_game():
    while True:
        choose = input(f"2 players or computer? [2/pc]\n> ")
        if choose == "2":
            game("X", "O", None)
        elif choose == "pc":
            game("X", None, "O")


def game(user_id, second_user_id, pc_id):
    count = 0
    grid_list = ["a", "b", "c",
                 "d", "e", "f",
                 "g", "h", "i"]
    grid_board = " a | b | c " \
                 "\n---|---|---" \
                 "\n d | e | f " \
                 "\n---|---|---" \
                 "\n g | h | i "
    while True:
        user = user_move(grid_list, grid_board)
        grid_list, grid_board = grid_updates(user, user_id, grid_list, grid_board, count)
        if second_user_id is None:
            pc = bot_move(grid_list)
            grid_list, grid_board = grid_updates(pc, pc_id, grid_list, grid_board, count)
        else:
            second_user = user_move(grid_list, grid_board)
            grid_list, grid_board = grid_updates(second_user, second_user_id, grid_list, grid_board, count)


def user_move(grid, board):
    while True:
        user_input = str(input(f'{board}\n> '))
        if user_input in grid:
            if user_input not in ["X", "O"]:
                return user_input


def bot_move(grid):
    while True:
        pc_input = str(random.choice(grid))
        if pc_input not in ["X", "O"]:
            return pc_input


def grid_updates(guest, guest_id, grid, board, count):
    grid = grid_list_update(guest, guest_id, grid)
    board = grid_board_update(guest, guest_id, board)
    is_win(guest_id, grid, count)
    return grid, board


def grid_list_update(guest, guest_id, grid):
    x = []
    for characters in grid:
        if characters != guest:
            x.append(characters)
        elif characters == guest:
            x.append(guest_id)
    grid = x
    return grid


def grid_board_update(guest, guest_id, board):
    board = str(board).replace(guest, guest_id)
    return board


def is_win(guest_id, grid, count):
    count += 1
    if (grid[0] == guest_id and grid[1] == guest_id and grid[2] == guest_id) \
            or (grid[3] == guest_id and grid[4] == guest_id and grid[5] == guest_id) \
            or (grid[6] == guest_id and grid[7] == guest_id and grid[8] == guest_id):
        print(f"{guest_id} has won in horizontal!")
        exit()
    elif (grid[0] == guest_id and grid[3] == guest_id and grid[6] == guest_id) \
            or (grid[1] == guest_id and grid[4] == guest_id and grid[7] == guest_id) \
            or (grid[2] == guest_id and grid[5] == guest_id and grid[8] == guest_id):
        print(f"{guest_id} has won in vertical!")
        exit()
    elif (grid[0] == guest_id and grid[4] == guest_id and grid[8] == guest_id) \
            or (grid[2] == guest_id and grid[4] == guest_id and grid[6] == guest_id):
        print(f"{guest_id} has won in diagonal!")
        exit()
    elif count == 9:
        print(f"Draw!")
    return count


choose_game()
