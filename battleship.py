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