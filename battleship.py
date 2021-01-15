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