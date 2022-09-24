# Week 2 - Tic Tac Toe
# Anna Varner - CSE 210



def main():   
    play_again = "y"
    while play_again == "y" or play_again == "Y":
        player = next_player("")
        board = drawgrid()
        while not (winner(board) or tie(board)):
            display_board(board)
            move(player, board)
            player = next_player(player)
        display_board(board)
        play_again = input("Game over! Would you like to play again? (y/n): ")

def drawgrid():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('- + - + -')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('- + - + -')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def tie(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    print()
    print("------------")        
    print("It's a tie!")
    return True 

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])



def move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"



if __name__ == "__main__":
    main()