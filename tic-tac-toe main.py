'''
 author: Stephen Stauffer
 assignment: tic-tac-toe
 '''


def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    player = next_player(player)
    display_board(board)
    if has_winner(board) == True:
        print(f"{player} is the Winner! ")
    else:
        print("It is a Draw!")
    print(f"Good game. Thank you for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    square = check_input(player, square, board)
    board[square - 1] = player

def check_input(player, square, board):
    if square in board:
        check = True
        return square
    else:
        check = False
        while check != True:
            print("Please check input.")
            square = int(input(f"{player}'s turn to choose a square (1-9): "))
            if square in board:
                check = True
            else:
                check = False
            return square

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()