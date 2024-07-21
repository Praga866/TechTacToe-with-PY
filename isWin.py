def get_valid_position():
    while True:
        try:
            pos = int(input("Enter the Position (1-9): "))
            if pos < 1 or pos > 9:
                print("Position must be between 1 and 9.")
            else:
                return pos
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def Find_position(val):
    # val = int(input("Enter the Position: "))
    val = val - 1
    pos = [val // 3, val % 3]
    return pos

def isWin(board):
    ret = [None, True]
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            ret[0] = row[0]
            ret[1] = False
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            ret[0] = board[0][col]
            ret[1] = False
    
    if board[0][0] == board[1][1] == board[2][2] != 0:
        ret[0] = board[0][0]
        ret[1] = False
    
    if board[0][2] == board[1][1] == board[2][0] != 0:
        ret[0] = board[0][0]
        ret[1] = False
    return ret

def print_Board(board):
    print("________________\n")
    for row in board:
        print(" ", end="")
        print("  |  ".join(map(str, row)),end="")
        print(" ")
        print("________________\n")

def print_Credits():
    print("\nFollow me on github: https://github.com/Praga866\nContact me on mail: pragaofficial004@gmail.com\nSupport by pullin the repos...\n")