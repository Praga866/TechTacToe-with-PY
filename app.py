import isWin as winner

previous_State = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

dec = None
#Confirm the Name
while(dec != "Y"):
    player_1,player_2 = input("Enter the Player 1 Name: ").upper(), input("Enter the Player 2 name: ").upper()
    print("{} is Player 1 {}\n{} is Player 2 {}\n\nConfirm?(Y/N)" .format(player_1, "== X ==", player_2, "== O =="))
    dec = input().upper()

winner.print_Board(previous_State)

current_State = previous_State
result = [0,True]

print()

while(result[1]):
    posX = winner.get_valid_position()
    val = winner.Find_position(posX)
    if(current_State[val[0]][val[1]] == 0):
        current_State[val[0]][val[1]] = "X"

    result = winner.isWin(current_State)
    winner.print_Board(current_State)
    if(result[1] == False):
        Win = player_1 if result[0] == "X" else player_2
        print("{} Wins the Match and holds the Cup....\nThe Other got face Planted 🤣😂\n\n".format(player_1))
        break


    posO = winner.get_valid_position()
    val = winner.Find_position(posO)
    if(current_State[val[0]][val[1]] == 0):
        current_State[val[0]][val[1]] = "O"

    result = winner.isWin(current_State)
    winner.print_Board(current_State)
    if(result[1] == False):
        Win = player_1 if result[0] == "X" else player_2
        print("{} Wins the Match and holds the Cup....\nThe Other got face Planted 🤣😂\n\n".format(player_2))
        break

winner.print_Credits()

