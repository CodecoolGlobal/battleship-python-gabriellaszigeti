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
        if user_input == "1" or user_input == "2" :
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
    user_input_in_touple = (ord(user_input.lower()[0]) - ord('a'), int(user_input[1:])-1)
    return user_input_in_touple
 
 
def header(board_size):
    '''Prints board header'''
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
        while True:
            print_board(board)
            print(f"{fleet}")
            print(f"\nYou are currently placing {part}\n")
            try:
                if player_name == {'AI'}:
                    row, col = ai_ship_placement(board)
                    chars = ["V", "H"]
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
                        if board[col + 1][row + j] == "X" or board[col - 1][row + j] == "X" or board[col][row + 1 + j] == "X" or board[col][row - 1 + j] == "X":
                            raise IndexError
                    for j in range(fleet[part]):
                        board[row][col + j] = "X"
                        fleet_coord.append([col, row + j])
                    break
                else:
                    clear()
                    for j in range(fleet[part]):
                        if board[row + j][col] == "X":
                            raise IndexError
                        if board[col - 1 + j][row] == "X" or board[col + 1 + j][row] == "X" or board[col - j][row - 1] == "X" or board[col + j][row + 1] == "X":
                            raise IndexError
                    for j in range(fleet[part]):
                        board[row + j][col] = "X"
                        fleet_coord.append([col + j, row])
                    # print(fleet_coord)
                    break
            except IndexError:
                print('Coordinate out of range')
    print_board(board)
    print("\nAll ships placed!\n")
    input("Press enter to continue...")
    clear()
    return board
 
 
def shooting_phase(board, hitboard, player_name):
    '''Marks input on hitboard if all parameters are ok'''
    while True:
        try:
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
                break
            elif board[row][col] == '0':
                hitboard[row][col] = 'M'
                print('You have missed it')
                break
        except IndexError:
            print('Coordinate out of range')
    return hitboard
 
 
def ai_ship_placement(board):
    '''returns a random value on board '''
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    return row, col
 
 
def get_ai_move(player_hit_board):
    '''simple ai tries to hit ship parts returns coords'''
    while True:
        try:
            for lists in player_hit_board:
                for element in lists:
                    if element == "H":
                        row = player_hit_board.index(lists)
                        col = lists.index(element) + 1
                        if player_hit_board[row][col] == "M":
                            col -= 1
                            row += 1
                        if player_hit_board[row][col] == "M":
                            row -= 2
                        if player_hit_board[row][col] == "M":
                            row += 1
                            col -= 1
                        return row, col
                    else:
                        raise IndexError
        except IndexError:
            row = random.randint(0, len(player_hit_board) - 1)
            col = random.randint(0, len(player_hit_board) - 1)
            print("Bad AI! Dumb move!")
            time.sleep(1)
            break
    return row, col
 
 
def get_direction():
    '''horizontal or vertical '''
    while True:
        direction = input("H for horizontal, V for vertical: \n").lower()
        if direction == "h" or direction == "v":
            return direction
        else:
            print("\nWrong input! :(\n")
 
 
def is_table_full(board):
    '''checks if table is full'''
    return any('0' in x for x in board)
 
 
def all_ship_sunk(board, sum_fleet):
    '''checks if all ships are sunk'''
    sunk_sum = 0
    for row in board:
        for i in row:
            if i == "H":
                sunk_sum += 1
    if sunk_sum == sum_fleet:
        return True
    else:
        return False
 
 
def rules():
    '''prints out rules+ascii art '''
    clear()
    print(battleship_art[7])
    print(battleship_rules[0])
    input("\nPress any key to continue...")
    clear()
 
 
def intro():
    '''Intro animation'''
    for i in range(3):
        for i in range(7):
            print("\033[0;34;48m \033")
            print(battleship_art[i])
            print("\033[0;37;48m\n")
            time.sleep(0.3)
            clear()
 
 
def outro():
    '''prints out Game over + ascii art'''
    clear()
    print("\033[0;34;48m \033")
    print(battleship_art[13])
    print(battleship_art[15])
 
 
def game_setup():
    '''gets standard setup'''
    setup = {}
    x = game_mode()
    if x == "1":
        setup["player1"] = get_player_name(1)
        setup["player2"] = "AI"
    elif x == "2":
        setup["player1"] = get_player_name(1)
        setup["player2"] = get_player_name(2)
    clear()
    print(f"{battleship_art[9]}\nPlease enter custom board size:\n\n")
    setup["board_size"] = get_custom_input(5,10)
    clear()
    print(battleship_art[10])
    print("Please enter turn limit:\n\n")
    setup["turn_limit"] = get_custom_input(5,50)
    return setup
 
 
def main():
    setup = game_setup()
    fleet = {"Carrier": 4, "Battleship": 3, "Cruiser": 2}
    sum_fleet = sum(fleet.values())
    player1_board = init_board(setup["board_size"])
    player2_board = copy.deepcopy(player1_board)
    player1_board_to_shoot = copy.deepcopy(player1_board)
    player2_board_to_shoot = copy.deepcopy(player1_board)
    print(f"{battleship_art[11]}\n{setup['player1']} get ready to placement phase!\n\n")
    input("Press enter to continue...")
    clear()
    player1_board = placement_phase(player1_board, fleet, {setup['player1']})
    print(f"{battleship_art[11]}\n{setup['player2']} get ready to placement phase!\n\n")
    input("Press enter to continue...")
    clear()
    player2_board = placement_phase(player2_board, fleet, {setup['player2']})
    v = True
    while v is True:
        clear()
        print(f"{setup['player1']}'s turn\nThis is Player1's board.\n")
        print_board(player1_board)
        print("This is your hit board.\n")
        player1_board_to_shoot = shooting_phase(player2_board, player1_board_to_shoot, {setup['player1']})
        clear()
        setup['turn_limit'] -=1
        print(f"{battleship_art[12]}\n{setup['player2']} get ready to shooting phase!\n\n")
        input("Press enter to continue...")
        if  is_table_full(player1_board_to_shoot) is False:
            v = False
            break
        if all_ship_sunk(player1_board_to_shoot, sum_fleet) is True:
            print("Player1 won!")
            time.sleep(2)
            v = False
            break
        print(f"{setup['player2']}'s turn.\nThis is player2's board.\n")
        print_board(player2_board)
        print("This is your hit board.\n")
        player2_board_to_shoot = shooting_phase(player1_board, player2_board_to_shoot, {setup['player2']})
        clear()
        setup['turn_limit'] -= 1
        print(f"{battleship_art[12]}{setup['player1']} get ready to shooting phase!\n\n")
        input("Press enter to continue...")
        if is_table_full(player2_board_to_shoot) is False:
            v = False
            break
        if all_ship_sunk(player2_board_to_shoot,sum_fleet) is True:
            print("Player2 won!")
            time.sleep(2)
            v = False
            break
        if setup['turn_limit'] == 0:
            print("No more turns, it's a draw!")
            v = False
            break
 
 
if __name__ == "__main__":
    intro()
    rules()
    main()
    outro()