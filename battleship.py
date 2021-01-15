'''
Battleship game
'''

import time
import os
import copy
import random
from string import ascii_uppercase
from battleship_ascii import battleship_art
from battleship_ascii import battleship_rules


def clear():
    '''clears console'''
    os.system("clear")


def get_player_name(numero):
    '''Gets player name takes NO. parameter'''
    clear()
    print(battleship_art[8])
    player_name = input(f"Please enter Player{numero} name: \n")
    clear()
    return player_name


def game_mode():
    '''returns single player or multiplayer option'''
    clear()
    print(battleship_art[14])
    while True:
        print("Press 1 to Single Player\n\n")
        print("Press 2 to Multiplayer ")
        user_input = input("")
        if user_input == "1" or user_input == "2":
            clear()
            return user_input


def init_board(board_size):
    '''Generates board'''
    board = []
    for i in range(0, board_size):
        board.append(["0"] * (board_size))
    return board


def ask_for_user_input():
    '''Asks for input checks if it"s on the table '''
    while True:
        try:
            user_input = input('Please enter the coordinates: ')
            if user_input[0].isalpha() == True and user_input[1].isdigit() == True and (user_input[1] != '0') == True:
                break
            else:
                print("You have entered invalid coordinates, please correct them.")
        except(IndexError, ValueError):
            print("You have entered invalid coordinates, please correct them.")
    user_input_in_touple = (
        ord(user_input.lower()[0]) - ord('a'), int(user_input[1:])-1)
    return user_input_in_touple


def header(board_size):
    '''Prints board header'''
    #print("\033[0;34;48m     Battleship Game  \n")
    print("🚢".ljust(2), end=" ")
    for i in range(1, board_size + 1):
        print(f"{i}" .ljust(3), end=" ")
    print("\n")


def print_board(board):
    '''Prints out Board'''
    header(len(board))
    for i in range(len(board)):
        row = "|".join(board[i])
        print(f"{ascii_uppercase[i].center(3)}", end=" " + " ".join(row))
        print("\n")


def get_custom_input(minimum, maximum):
    '''Used to get input checks if it is beteween mininmum and maximum parameter'''
    while True:
        try:
            user_input = int(
                input(f"Please enter a number between {minimum}-{maximum}): \n"))
            if user_input >= minimum and user_input <= maximum:
                clear()
                return user_input
            else:
                print(
                    f"Invalid input! (must be a number between {minimum}-{maximum})")
        except ValueError:
            print(
                f"Invalid input! (must be a number between {minimum}-{maximum})")
    clear()
    return user_input


def placement_phase(board, fleet, player_name):
    '''places ships on board'''
    fleet_coord = []
    for part in fleet:
        ship_coord = {}
        while True:
            print_board(board)
            print(f"{fleet}")
            print(f"\nYou are currently placing {part}\n")
            try:
                if player_name == {'AI'}:
                    row, col = ai_ship_placement(board)
                    chars = ["v", "h"]
                    direction = random.choice(chars)
                else:
                    user_input = ask_for_user_input()
                    row = user_input[0]
                    col = user_input[1]
                    direction = get_direction()
                if direction == "h":
                    clear()
                    for j in range(fleet[part]):
                        if board[row][col + j] == "X":
                            raise IndexError
                        if row != 0 and row != len(board) - 1:
                            if board[row - 1][col + j] == "X" or board[row + 1][col + j] == "X":
                                raise IndexError
                    for j in range(fleet[part]):
                        board[row][col + j] = "X"
                        coord = str(row) + str(col + j)
                        ship_coord[coord] = "C"
                    fleet_coord.append(ship_coord)
                    print("\n*For Demo purposes only* Ship position: C-clear D-damaged S-sunk")
                    print(fleet_coord)
                    break
                elif direction == "v":
                    clear()
                    for j in range(fleet[part]):
                        if board[row + j][col] == "X":
                            raise IndexError
                        if col != 0 and col != len(board) - 1:
                            if board[row + j][col - 1] == "X" or board[row + j][col + 1] == "X":
                                raise IndexError
                    for j in range(fleet[part]):
                        board[row + j][col] = "X"
                        coord = str(row + j) + str(col)
                        ship_coord[coord] = "C"
                    fleet_coord.append(ship_coord)
                    print("\n*For Demo purposes only* Ship position: C-clear D-damaged S-sunk")
                    print(fleet_coord)
                    break
            except IndexError:
                print('Coordinate Error')
    print_board(board)
    print("\nAll ships placed!\n")
    input("Press enter to continue...")
    clear()
    return board, fleet_coord


def shooting_phase(board, hitboard, player_name, fleet_coord):
    '''Marks input on hitboard if all parameters are ok'''
    while True:
        try:
            print("\n*For Demo purposes only* Ship position: C-clear D-damaged S-sunk")
            print(fleet_coord)
            print_board(hitboard)
            if player_name == {'AI'}:
                row, col = get_ai_move(hitboard)
            else:
                user_input = ask_for_user_input()
                row = user_input[0]
                col = user_input[1]
            if hitboard[row][col] == 'H' or hitboard[row][col] == 'S' or hitboard[row][col] == 'M':
                print('You already placed in this field.')
                continue
            elif board[row][col] == 'X':
                hitboard[row][col] = 'H'
                print('You have hit a ship')
                coord = str(row) + str(col)
                for i in fleet_coord:
                    i[coord] = "D"
                break
            elif board[row][col] == '0':
                hitboard[row][col] = 'M'
                print('You have missed it')
                break
        except IndexError:
            print('Coordinate out of range')
    return hitboard, fleet_coord


def is_sunk(fleet_coord, boards):
    for dictionary in fleet_coord:
        if (all(value == 'D' for value in dictionary.values())):
            for x in dictionary.keys():
                row = int(x[0])
                col = int(x[1])
                boards[row][col] = "S"
    print(boards)
    return boards, fleet_coord


def ai_ship_placement(board):
    '''returns a random value on board '''
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    return row, col