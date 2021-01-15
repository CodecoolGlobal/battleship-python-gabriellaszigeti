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