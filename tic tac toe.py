#board
#display board
#play game
#handle turn
#check win
  #check rows
  #check columns
  #chcek diagonals
#check tie
#flip player
#--------global varibale-----
board=["_","_","_",
       "_","_","_",
       "_","_","_"]


#if game is still going
game_still_going = True

#who won? or tie?

winner=None

#whos turn is it
current_player= "X"

#display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play a game of tic toc toe
def play_game():

    #display the initial board
    display_board()

    #while the game is still going
    while game_still_going:

        #handle a sinle turn of an arbitary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

    #the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won ")
    elif winner== None:
        print(" tie ")

#handle a single turn of an arbitary player
def handle_turn(player):

    print(player + "'s turn")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("invalid input. choose a position from 1-9")
        position = int(position) - 1

        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. go again")

    board[position]= player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner = None
    return

def check_rows():
    #set up global variables
    global game_still_going
    #check if any of the row have same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    #if any row does have a match, flag that there was a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner(X OR O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the column have same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    # if any column does have a match, flag that there was a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner(X OR O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagonal have same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"

    # if any diagonal does have a match, flag that there was a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner(X OR O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
    return

def flip_player():
    #global variables we need
    global current_player
    #if the current player was X , then change it to O
    if current_player == "X":
        current_player = "O"
        #if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()