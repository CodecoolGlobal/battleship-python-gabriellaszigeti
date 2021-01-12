
from string import ascii_uppercase


board = []
board_size = 5


def init_board(board_size):
    for i in range(0, board_size):
        board.append(["0 "] * (board_size))
    return board


def header(board):
    print("🚢 ".rjust(2), end="")
    for i in range(1, board_size + 1):
        print(f"{i}" .rjust(2), end=" ")
    print("\n")
    

def print_board(board, board_size):
    for i in range(0, board_size):
        row = board[i]
        print(f"{ascii_uppercase[i].center(3)}", end=" " + " ".join(row))
        #print("-+-".join(row))
        print("\n")




init_board(5)
header(board)
print_board(board,board_size)
