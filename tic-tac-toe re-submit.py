'''
 author: Stephen Stauffer
 assignment: tic-tac-toe
 '''


def main():
    turn = 0
    player = "x"
    board = get_board()
    while not (three_in_a_row(board) or is_a_draw(turn)):
        display_board(board)
        make_move(player, board)
        player = swap_players(player)
        turn += 1
    player = swap_players(player)
    if three_in_a_row(board) == True and is_a_draw(turn) == False:
        print(f"Player {player} has won!")
    else:
        print("It is a draw!")
    print("Game over")
     
    
def get_board():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print(f"-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print(f"-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
    
def make_move(player, board):
    move = int(input(f"It is {player} turn. Please select a square (1-9). "))
    move = check_input(player, move, board)
    board[move - 1] = player

def swap_players(player):
    if player == "x":
        return "o"
    else:
        return "x"

def is_a_draw(turn):
    turn += 1
    if turn <= 9:
        return False
    return turn
    
def three_in_a_row(board):
    #across
    if board[0] == board[1] == board[2] != ' ':
        return True  
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    #up and down
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    #diagnol
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True

def check_input(player, square, board):
    if square in board:
        check = True
        return square
    else:
        square = False
        while check != True:
            print("Please check input.")
            square = int(input(f"{player}'s turn to choose a square (1-9): "))
            if square in board:
                check = True
            else:
                check = False
            return square
        
main()