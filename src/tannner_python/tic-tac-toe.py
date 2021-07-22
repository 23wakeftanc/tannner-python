#tic-tac-toe board

"""
[
    [-,-,-,]
    [-,-,-,]
    [-,-,-,]
]
user input -> enters something 1-9
if they enter anything else, tell them to go again
check user_input to see if that spot is already taken
add it to the board
check if the user won: check rows, coluomns and diagonal
toggle between users after sucussful moves

"""
board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

user = True #when true refers to "x", otherwise refers to "o"
turn = 0
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
    if user_input == "q":
        print("Thanks for playng!")
        return False
    else: return True

def check_input(user_input):
    #check if its a number
    if not isnum(user_input): return False
    user_input = int(user_input)
    #check if its a number 1-9
    if not bounds(user_input): return False
    
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_input):
    if user_input>9 or user_input<1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row] [col] != "_":
        print("That position is taken")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(user_input % 3) 
    return (row, col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col]= active_user

def current_user(user):
    if user == True: return "x"
    else: return "o"

def iswin(user, board):
    if check_row(user, board): return True
    if check_colummn(user,board): return True
    if check_diagonal(user, board): return True
    else: return False

def check_diagonal(user, board):
    #top left to bottom rigt
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False

def check_colummn(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

while turn < 9:
    active_user = current_user(user)
    print_board(board)
    user_input=input("Please enter a postition 1 through 9 or enter \"q\" to quit: ")
    if not quit(user_input): break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break
    

    turn += 1
    if turn == 9: print("Draw!")
    user = not user