

def game():
    user_turns()


def user_turns():
    user_id, second_user_id = "X", "O"  # x o
    grid_list = [[None, None, None], [None, None, None], [None, None, None]]
    while True:
        # first user turn
        guest_move(grid_list, user_id)
        if is_win(user_id, grid_list):  #
            print(f'{user_id} has won')
            exit()
        # second user turn
        guest_move(grid_list, second_user_id)
        if is_win(second_user_id, grid_list):  # if the returned value from is_win is True, then it prints out
            print(f'{second_user_id} has won')
            exit()


def guest_move(grid, guest_id):
    while True:
        count = 0
        if count == 9:  # if they played 9 times it stops the game (no positions open)
            exit()
        user_input = str(input(f'\n{grid[0]}\n{grid[1]}\n{grid[2]}\n{guest_id}: '))
        if user_input in ["11", "12", "13", "21", "22", "23", "31", "32", "33"]:  # limited positions
            # if the user gives a higher number -> out
            if move_return(user_input, guest_id, grid):  # then if move_return return true it assigns
                grid = move_return(user_input, guest_id, grid)  # it assigns grid to the returned value which is in func
                return grid
        count += 1


def move_return(guest, guest_id, grid):
    guest = list(guest)  # getting the row and the col separated in a list then assigning them to row and col var
    row = int(guest[0]) - 1  # because the input could be row 1 col 2 but the real numbers should be row 0 and col 1
    col = int(guest[1]) - 1
    if grid[row][col] is None:  # checking if a position is open
        grid[row][col] = guest_id
        return True, grid


def is_win(guest_id, grid):
    # diagonal is_win loop:
    if (grid[0][0] == guest_id and grid[1][1] == guest_id and grid[2][2] == guest_id)\
            or (grid[0][0] == guest_id and grid[1][1] == guest_id and grid[2][2] == guest_id):  # manual stuff
        return True
    # horizontal is_win loop:
    guest_count = 0
    for x in grid:  # which is all the arrays inside (2d) the main array [ [ ], [ ], [ ] ]
        for y in x:  # which is all the characters inside the inside arrays [ ]
            if y == guest_id:  # for example if y is equal to "X" it adds 1 to the count
                guest_count += 1
        if guest_count == 3:  # if three consecutive "X" (example) appears in a row, it returns True
            return True
        guest_count = 0
    # vertical is_win loop:
    for x in range(len(grid)):  # which is the length of the array (so it loop through three times)
        for y in grid:  # which is all the characters inside the inside arrays
            if y[x - 1] == guest_id:  # then it compares the first character of the first row, the second and the last
                guest_count += 1
        if guest_count == 3:
            return True
        guest_count = 0
    return False  # <- when nothing is returned, it obviously returns False


game()
