# Define possible inputs as corresponding numbers to 3x3 grid
possible_inputs = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def game_loop(): # Main loop
    players = ('X','O') # Tuple with both players
    grid_list = [[None, None, None],[None, None, None],[None, None, None]]
    for i in range(9): # Max 9 moves
        grid_list = guest_move(grid_list, players[i%2]) # Update grid based on move
        try: # is_win will give an exception if there is no win, otherwise return winner and quit loop
            print(is_win(players[i%2], grid_list))
            break
        except: pass

def guest_move(grid, guest): # here is where we take the move and apply it to the board
        user_input = input(f'\n{grid[0]}\n{grid[1]}\n{grid[2]}\n{guest}: ')
        while user_input not in possible_inputs: # reference to list of positions left
                user_input = input("\nTry agian: ")
        possible_inputs.remove(user_input) 
        grid[int(user_input[0])-1][int(user_input[1])-1] = guest # convert 2 didget input to position on array
        return grid
                
def is_win(guest_id, grid): # Checks win, there is some room for optimization here, mostly left as is
    if (grid[0][0] == grid[1][1] == grid[2][2] == guest_id) or (grid[0][2] == grid[1][1] == grid[2][0] == guest_id):  # manual stuff
        return "Player " + guest_id + " has won!"
    # horizontal is_win loop:
    for x in grid:  # which is all the arrays inside (2d) the main array [ [ ], [ ], [ ] ]
        guest_count = 0
        for y in x:  # which is all the characters inside the inside arrays [ ]
            if y == guest_id:  # for example if y is equal to "X" it adds 1 to the count
                guest_count += 1
        if guest_count == 3:  # if three consecutive "X" (example) appears in a row, it returns True
            return"Player " + guest_id + " has won!"
    # vertical is_win loop:
    for x in range(len(grid)):  # which is the length of the array (so it loop through three times)
        guest_count = 0
        for y in grid:  # which is all the characters inside the inside arrays
            if y[x - 1] == guest_id:  # then it compares the first character of the first row, the second and the last
                guest_count += 1
        if guest_count == 3:
            return "Player " + guest_id + " has won!"
    raise Exception  # fast way to express nobody has won

if __name__ == "__main__":
    game_loop()
