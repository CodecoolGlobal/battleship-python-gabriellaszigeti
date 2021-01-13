from string import ascii_uppercase


board = []
board_size = 5


def init_board(board_size):
    for i in range(0, board_size):
        board.append(["0"] * (board_size))
    return board


def header(board):
    print("\033[0;34;48m     Battleship Game  \n")
    print("🚢".ljust(2), end=" ")
    for i in range(1, board_size + 1):
        print(f"{i}" .ljust(3), end=" ")
    print("\n")


def print_board(board, board_size):
    for i in range(0, board_size):
        row = "|".join(board[i])
        print(f"{ascii_uppercase[i].center(3)}", end=" " + " ".join(row))
        print("\n")



init_board(5)
header(board)
board[0][3] = "H"
board[2][3] = "M"
board[3][1] = "B"
print_board(board,board_size)
