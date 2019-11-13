
board = [[" "," "," "],[" "," "," "],[" "," "," "],]

def move(player, location, board=board):
    num_spaces = len(board[0]) + len(board[1]) + len(board[2])

    try:
        if len(board) != 3:
            print("Board size is incorrect.")
        elif num_spaces != 9:
            print("Board size is incorrect.")
        else:
            board[location[0]][location[1]] = player
            print_board(board)
    except IndexError:
        if len(location) != 2:
            print("Location is invalid. Two coordinates are required.")
        elif location[0] > 2 or location[1] > 2:
            print("Location is invalid. Coordinates cannot be greater than two. ")

def print_board(board):
    print(board[0]), print(board[1]), print(board[2])

status = True
while True:
    board = [[" "," "," "],[" "," "," "],[" "," "," "],]
    player1 = "X"
    player2 = "Y"

    player = input("Player1 or Player2? ")
    location = input("Enter move coordinates (x, y): ")
    
    move(player1, (0, 0))



# move(board, (0, 2), player1)







    
