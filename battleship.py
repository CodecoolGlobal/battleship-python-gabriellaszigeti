import time
import os
import copy
from string import ascii_uppercase
from battleship_ascii import battleship_art
from battleship_ascii import battleship_rules
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


def print_board(board, player):
    print(f"\n{player}'s turn!\n")
    print_board_header(len(board))
    print_board_row(board)


def get_direction():
    while True:
        direction = input("H for horizontal, V for vertical: ").lower()
        if direction == "h" or direction == "v":
            return direction
        else:
            print("Wrong input! :(")


def get_input(board):
    while True:
        player_move = input(
            "Enter a coordinate!:\nsyntax: First char letter, second char number: ")
        columns = range(1, len(board) + 1)
        try:
            letter, number = player_move[0].upper(), int(player_move[1:])
            row, column = columns.index(number), ascii_uppercase.index(letter)
            if player_move == "quit":
                clear()
                exit()
            if board[column][row] == "X":
                continue
            if row < len(board) and column < len(board):
                break
            else:
                print("wrong input, not on board!")
                time.sleep(2)
        except (ValueError, IndexError):
            print("wrong input WTF?!")
            time.sleep(2)
            continue
    return row, column


def get_custom_input(minimum, maximum):
    while True:
        try:
            user_input = int(
                input(f"Please enter a number between {minimum}-{maximum}): \n"))
            if user_input >= minimum and user_input <= maximum:
                return user_input
            else:
                print(
                    f"Invalid input! (must be a number between {minimum}-{maximum})")
        except ValueError:
            print(
                f"Invalid input! (must be a number between {minimum}-{maximum})")
    return user_input


def placement_stage(board, player, fleet):
    fleet_copy = fleet.copy()
    fleet_coord = []
    for part in fleet_copy:
        print_board(board, player)
        print(f"{fleet}")
        print(f"You are currently placing {part}")
        while True:
            try:
                row, col = get_input(board)
                direction = get_direction()
                if direction == "h":
                    for i in range(fleet_copy[part]):
                        if board[col][row + i] == "X":
                            raise IndexError
                        if board[col + 1][row + i] == "X" or board[col - 1][row + i] == "X" or board[col][row + 1 + i] == "X" or board[col][row - 1 + i] == "X":
                            raise IndexError
                    for i in range(fleet_copy[part]):
                        board[col][row + i] = "X"
                        fleet_coord.append([col, row + i])
                    print(fleet_coord)
                    break
                else:
                    for i in range(fleet_copy[part]):
                        if board[col+i][row] == "X":
                            raise IndexError
                        if board[col - 1 + i][row] == "X" or board[col + 1 + i][row] == "X" or board[col - i][row - 1] == "X" or board[col + i][row + 1] == "X":
                            raise IndexError
                    for i in range(fleet_copy[part]):
                        board[col + i][row] = "X"
                        fleet_coord.append([col + i, row])
                    print(fleet_coord)
                    break
                print("\nChanging ships\n")
            except IndexError:
                print("Invalid input!")
                time.sleep(2)
    print_board(board, player)
    print("\nAll ships placed!\n")
    input("Press enter to continue...")
    return board


def shooting_phase(player_board, player_hit_board, player):
    print_board(player_hit_board, player)
    row, col = get_input(player_hit_board)
    if player_board[col][row] == "X":
        print("hit!")
        player_hit_board[col][row] = "H"
    elif player_board[col][row] == "H" or player_board[col][row] == "M" or player_board[col][row] == "S":
        print("Yo what?")
    else:
        player_hit_board[col][row] = "M"
    print_board(player_hit_board, player)
    input("Press enter to continue...")
    return player_hit_board


def is_table_full(board):
    return any('0' in x for x in board)


def all_ship_sunk(board, sum_fleet):
    sunk_sum = 0
    for row in board:
        for i in row:
            if i == "S":
                sunk_sum += 1
    if sunk_sum == sum_fleet:
        return True
    else:
        return False


def intro():
    # prints out some badass colored ascii animation
    clear()
    for i in range(10):
        for i in range(7):
            print(battleship_art[i])
            time.sleep(0.3)
            clear()


def rules():
    # prints out rules+ascii art
    clear()
    print(battleship_art[7])
    print(battleship_rules[0])
    input("\nPress any key to continue...")


def outro():
    # prints out Game over + ascii art + Turns left?
    pass


def game_setup():
    setup = {}
    # setup["player1"] = get_player_name(1)
    # setup["player2"] = get_player_name(2)
    setup["player1"] = "Bob"
    setup["player2"] = "Joe"
    print("Please enter custom board size:\n\n")
    # setup["board_size"] = get_custom_input(5,10)
    setup["board_size"] = 10
    clear()
    print("Please enter turn limit:\n\n")
    # setup["turn_limit"] = get_custom_input(5,50)
    setup["turn_limit"] = 50
    print(setup)
    return setup


def main():
    setup = game_setup()
    fleet = {"Carrier": 4, "Battleship": 3, "Cruiser": 2}
    sum_fleet = sum(fleet.values())
    player1_board = generate_board(setup["board_size"])
    player2_board = copy.deepcopy(player1_board)
    player1_hit_board = copy.deepcopy(player1_board)
    player2_hit_board = copy.deepcopy(player1_board)
    clear()
    print(f"{setup['player1']} get ready to placement phase!")
    input("Press enter to continue...")
    clear()
    player1_board = placement_stage(player1_board, setup['player1'], fleet)
    clear()
    print(f"{setup['player2']} get ready to placement phase!")
    input("Press enter to continue...")
    clear()
    player2_board = placement_stage(player2_board, setup['player2'], fleet)
    clear()
    end = True
    while end:
        print(
            f"{setup['player1']} get ready to shooting phase! Turns left: {setup['turn_limit']}")
        input("Press enter to continue...")
        clear()
        player1_hit_board = shooting_phase(
            player2_board, player1_hit_board, setup['player1'])
        setup['turn_limit'] -= 1
        clear()
        if all_ship_sunk(player1_hit_board, sum_fleet) is True:
            print(f"Player {setup['player1']} won!")
            end = False
        end = is_table_full(player1_hit_board)
        print(
            f"{setup['player2']} get ready to shooting phase! Turns left: {setup['turn_limit']}")
        input("Press enter to continue...")
        clear()
        player2_hit_board = shooting_phase(
            player1_board, player2_hit_board, setup['player2'])
        setup['turn_limit'] -= 1
        clear()
        end = is_table_full(player2_hit_board)
        if all_ship_sunk(player2_hit_board, sum_fleet) is True:
            print(f"Player {setup['player2']} won!")
            end = False
        if setup['turn_limit'] == 0:
            print("No more turns, it's a draw!")
            end = False


if __name__ == "__main__":
    # intro()
    # rules()
    main()
    outro()
