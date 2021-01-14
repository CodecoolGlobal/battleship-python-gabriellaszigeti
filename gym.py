import time
import os
import copy
import random
from string import ascii_uppercase
from battleship_ascii import battleship_art
from battleship_ascii import battleship_rules
 
 
def clear():
    os.system("clear")

 
def get_player_name(numero):
    clear()
    print(battleship_art[8])
    player_name = input(f"Please enter Player{numero} name: \n")
    return player_name

    #print("\033[0;34;48m     Battleship Game  n\")

def init_board(board_size):
    board = []
    for i in range(0, board_size):
        board.append(["0"] * (board_size))
    return board
 

def ask_for_user_input():
    while True:
        try:
            user_input = input('Please enter the coordinates:')
            if user_input[0].isalpha() == True and user_input[1].isdigit() == True and (user_input[1] != '0') == True:
                break
            else:
                print("You have entered invalid coordinates, please correct them.")
        except(IndexError,ValueError):
            print("You have entered invalid coordinates, please correct them.")
    user_input_in_touple = (ord(user_input.lower()[0]) - ord('a'), int(user_input[1:])-1)
    return user_input_in_touple


def header(board_size):
    #print("\033[0;34;48m     Battleship Game  \n")
    print("🚢".ljust(2), end=" ")
    for i in range(1, board_size + 1):
        print(f"{i}" .ljust(3), end=" ")
    print("\n")
 
 
def print_board(board):
    header(len(board))
    for i in range(len(board)):
        row = "|".join(board[i])
        print(f"{ascii_uppercase[i].center(3)}", end=" " + " ".join(row))
        print("\n")
 

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
 
 
def placement_phase(board, fleet):
    for part in fleet:
        print_board(board)
        print(f"{fleet}")
        print(f"You are currently placing {part}")
        while True:
            try:
                user_input = ask_for_user_input()
                row = user_input[0]
                col = user_input[1]
                direction = get_direction()
                if direction == "h":
                    for j in range(fleet[part]):
                        if board[row][col + j] == "X":
                            raise IndexError
                    for j in range(fleet[part]):
                        board[row][col + j] = "X"
                    break
                else:
                    for j in range(fleet[part]):
                        if board[row + j][col] == "X":
                            raise IndexError
                    for j in range(fleet[part]):
                        board[row + j][col] = "X"
                    break
            except IndexError:
                print('Coordinate out of range')
    print_board(board)
    print("\nAll ships placed!\n")
    input("Press enter to continue...")
    return board 





def shooting_phase(board, hitboard):
    while True:
        try:
            print_board(hitboard)
            user_input = ask_for_user_input()
            row = user_input[0]
            col = user_input[1]
            if hitboard[row][col] == 'H' or hitboard[row][col] == 'S' or hitboard[row][col] == 'M':
                print('You already placed in this field.')
                #clear()
                continue
            elif board[row][col] == 'X':
                hitboard[row][col] = 'H'
                print('You have hit a ship')
                return hitboard
            elif board[row][col] == '0':
                hitboard[row][col] = 'M'
                print('You have missed it')
                return hitboard
        except IndexError:
            print('Coordinate out of range')

 

def get_direction():
    while True:
        direction = input("H for horizontal, V for vertical: ").lower()
        if direction == "h" or direction == "v":
            return direction
        else:
            print("Wrong input! :(")
 

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


def rules():
    clear()
    print("\033[0;34;48m\n")
    print(battleship_art[7])
    print(battleship_rules[0])
    input("\nPress any key to continue...")
 

def intro():
    for i in range(5):
        for i in range(7):
            print("\033[0;36;48m\n")
            print(battleship_art[i])
            time.sleep(0.3)
            clear()


def outro():
    clear()
    print(battleship_art[13])
    print(battleship_art[14])
    # prints out Game over + ascii art + Turns left?
    
 

def game_setup():
    setup = {}
    #setup["player1"] = get_player_name(1)
    #setup["player2"] = get_player_name(2)
    setup["player1"] = "Player1"
    setup["player2"] = "Player2"
    print(battleship_art[9])
    print("Please enter custom board size:\n\n")
    #setup["board_size"] = get_custom_input(5,10)
    setup["board_size"] = 5
    clear()
    print(battleship_art[10])
    print("Please enter turn limit:\n\n")
    #setup["turn_limit"] = get_custom_input(5,50)
    setup["turn_limit"] = 50
    print(setup)
    return setup

 
def main():
    #print("\033[0;34;48m\n")
    setup = game_setup()
    fleet = {"Battleship": 3}
    sum_fleet = sum(fleet.values())
    player1_board = init_board(setup["board_size"])
    player2_board = copy.deepcopy(player1_board)
    player1_board_to_shoot = copy.deepcopy(player1_board)
    player2_board_to_shoot = copy.deepcopy(player1_board)
    print_board(player1_board_to_shoot)
    clear()
    print("\033[0;34;48m\n")
    print(battleship_art[11])
    #print("\033[0;36;48m\n")
    print(f"{setup['player1']} get ready to placement phase!\n\n")
    input("Press enter to continue...")
    clear()
    player1_board = placement_phase(player1_board, fleet)
    clear()
    print("\033[0;34;48m\n")
    print(battleship_art[11])
    #print("\033[0;37;48m\n")
    print(f"{setup['player2']} get ready to placement phase!\n\n")
    input("Press enter to continue...")
    clear()
    player2_board = placement_phase(player2_board, fleet)
    clear()
    v = True
    while v == True:
        print("\033[0;34;48m\n")
        print(battleship_art[12])
        print(f"{setup['player1']} get ready to shooting phase!\n\n")
        input("Press enter to continue...")
        clear()
        print("\033[0;36;48m\n")
        print(f"{setup['player1']} 's turn\n")
        print("This is Player1's board.\n")
        print_board(player1_board)
        print("This is your hit board.\n")
        player1_board_to_shoot = shooting_phase(player2_board, player1_board_to_shoot)
        clear()
        print("\033[0;34;48m\n")
        print(battleship_art[12])
        #print("\033[0;33;48m\n")
        print(f"{setup['player2']} get ready to shooting phase!\n\n")
        input("Press enter to continue...")
        clear()
        if  is_table_full(player1_board_to_shoot) == False:
            break
        if all_ship_sunk(player1_board_to_shoot, sum_fleet) == True:
            break
        print("\033[0;33;48m\n")
        print(f"{setup['player2']} 's turn.\n")
        print("This is player2's board.\n")
        print_board(player2_board)
        print("This is your hit board.\n")
        player2_board_to_shoot = shooting_phase(player1_board, player2_board_to_shoot)
        clear()
        print("\033[0;34;48m\n")
        print(battleship_art[12])
        print(f"{setup['player1']} get ready to shooting phase!\n\n")
        input("Press enter to continue...")
        clear()
        if is_table_full(player2_board_to_shoot) == False:
            break
        if all_ship_sunk(player2_board_to_shoot,sum_fleet) == True:
            break




if __name__ == "__main__":
    #intro()
    rules()
    main()
    outro()