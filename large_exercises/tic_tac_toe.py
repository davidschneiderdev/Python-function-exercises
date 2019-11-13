
board = [[" "," "," "],[" "," "," "],[" "," "," "],]

def print_board(board):
    print(board[0]), print(board[1]), print(board[2])

def y_coordinate_reassign(y_coordinate):
    if y_coordinate == 0:
        return 2
    elif y_coordinate == 1:
        return y_coordinate
    else:
        return 0

def check_connect_three(moves_list):

    move_dictionary = {
        "(0, 0)":"1", "(0, 1)":"2", "(0, 2)":"3", "(1, 0)":"4", "(1, 1)":"5", "(1, 2)":"6", "(2, 0)":"7", "(2, 1)":"8", "(2, 2)":"9"
    }

    moves_string = ""

    for lst in moves_list:
        for move in lst:
            moves_string += str(move)
            # print(str(move))

    for key in move_dictionary.keys():
        moves_string = moves_string.replace(key, move_dictionary[key])

    # print(moves_string)
    #down win
    down_win1 = ['1', '4', '7']
    down_win2 = ['2', '5', '8']
    down_win3 = ['3', '6', '9']

    if all(x in moves_string for x in down_win1):
        print("You win!")
        return True
    elif all(x in moves_string for x in down_win2):
        print("You win!")
        return True
    elif all(x in moves_string for x in down_win3):
        print("You win!")
        return True

    #across win
    across_win1 = ['1', '2', '3']
    across_win2 = ['4', '5', '6']
    across_win3 = ['7', '8', '9']

    if all(x in moves_string for x in across_win1):
        print("You win!")
        return True
    elif all(x in moves_string for x in across_win2):
        print("You win!")
        return True
    elif all(x in moves_string for x in across_win3):
        print("You win!")
        return True

    #diagonal win

    diagonal_win1 = ['1', '5', '9']
    diagonal_win2 = ['7', '5', '3']

    if all(x in moves_string for x in diagonal_win1):
        print("You win!")
        return True
    elif all(x in moves_string for x in diagonal_win2):
        print("You win!")
        return True

def check_win(board):

    player1_moves_list = []
    player1_moves_list.append([(lst, item.index("X")) for lst, item in enumerate(board) if "X" in item])
    
    player2_moves_list = []
    player2_moves_list.append([(lst, item.index("O")) for lst, item in enumerate(board) if "O" in item])
    
    # print(f"player1 moves: {player1_moves_list}")
    # print(f"player2 moves: {player2_moves_list}")

    check_connect_three(player1_moves_list)
    check_connect_three(player2_moves_list)
    
def move(player, location, board=board):

    num_spaces = len(board[0]) + len(board[1]) + len(board[2])

    try:
        if len(board) != 3:
            print("Board size is incorrect.")
        elif num_spaces != 9:
            print("Board size is incorrect.")
        elif board[location[0]][location[1]] == "X" or board[location[0]][location[1]] == "O":
            print("Spot occupied. Try again.")
        else:
            board[location[0]][location[1]] = player
            return board

    except IndexError:
        if len(location) != 2:
            print("Location is invalid. Two coordinates are required.")
        elif location[0] > 2 or location[1] > 2:
            print("Location is invalid. Coordinates cannot be greater than two. ")

status = True
while status:
    should_restart = True
    while should_restart:
        should_restart = False
        player = input("player1 or player2? ")
        if player == "player1":
            player = 'X'
        elif player == "player2":
            player = 'O'
        else:
            print("Please enter valid player name.")
            should_restart = True
        x_coordinate = int(input("Enter x-coordinate: "))
        y_coordinate = int(input("Enter y-coordinate: "))
        reversed_y_coordinate = y_coordinate_reassign(y_coordinate)
        updated_board = move(player, (reversed_y_coordinate, x_coordinate))
        print_board(updated_board)
        check_win(updated_board)
















    
