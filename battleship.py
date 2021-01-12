import time
import os
import copy
from string import ascii_uppercase
# import ascii_art from another file
# import rules from the upper file just another variable


def clear():
    os.system("clear")


def get_player_name(numero):
    clear()
    player_name = input(f"Please enter Player{numero} name: \n")
    return player_name


def generate_board(board_size):
    board = []
    for _ in range(board_size):
        row = []
        for _ in range(board_size):
            row.append("0")
        board.append(row)
    return board


def print_board_header(board_size):
    print("".rjust(2), end="")
    for i in range(1, board_size + 1):
        print(f"{i}".rjust(4), end="")
    print("\n")


def print_board_row(board):
    board_size = len(board)
    for i in range(board_size):
        row = " | ".join(board[i])
        print(f"{ascii_uppercase[i].center(4)} {row}")
        
        
        if i != board_size - 1:
            print(" ".rjust(4), end="---")
            for i in range(1, board_size):
                print("", end="+---")
        print()


def print_board(board):
    print_board_header(len(board))
    print_board_row(board)


def get_custom_input(minimum, maximum):
    while True:
        try:
            user_input = int(input(f"Please enter a number between {minimum}-{maximum}): \n"))
            if user_input >= minimum and user_input <= maximum:
                return user_input
            else:
                print(f"Invalid input! (must be a number between {minimum}-{maximum})")
        except ValueError:
            print(f"Invalid input! (must be a number between {minimum}-{maximum})")
    return user_input


def is_table_full(board):
    for row in board:
        for col in row:
            if col == "0":
                return False
    return True


def all_ship_sunk(board):
    sunk_sum = 0
    for row in board:
        for i in row:
            if i == "S":
                sunk_sum += 1
    if sunk_sum == 9: # Total of ship parts
        return True
    else:
        return False


def intro():
    # prints out some badass colored ascii animation
    pass


def rules():
    # prints out rules+ascii art
    pass


def outro():
     # prints out Game over + ascii art + Turns left?
    pass


def game_setup():
    setup = {}
    setup["player1"] = get_player_name(1)
    setup["player2"] = get_player_name(2)
    print("Please enter custom board size:\n\n")
    setup["board_size"] = get_custom_input(5,10)
    clear()
    print("Please enter turn limit:\n\n")
    setup["turn_limit"] = get_custom_input(5,50)
    print(setup)
    return setup


def main():
    setup = game_setup()
    player1_board = generate_board(setup["board_size"])
    player2_board = copy.deepcopy(player1_board)
    print_board(player1_board)
    print_board(player2_board)


if __name__ == "__main__":
    intro()
    rules()
    main()
    outro()
