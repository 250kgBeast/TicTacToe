start = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
board = [
    [1, 3], [2, 3], [3, 3],
    [1, 2], [2, 2], [3, 2],
    [1, 1], [2, 1], [3, 1]
]
win = []
print(f"---------\n| {start[0]} {start[1]} {start[2]} |\n| {start[3]} {start[4]} {start[5]} |\n"
      f"| {start[6]} {start[7]} {start[8]} |\n---------")

game_loop = True
player_turn = True
while game_loop:
    if player_turn:
        turn = "X"
    else:
        turn = "O"
    coordinates = input("Enter the coordinates: ").split()
    coordinates_list = []
    for i in coordinates:
        try:
            if int(i) > 3:
                print("Coordinates should be from 1 to 3!")
                coordinates_list = []
                break
            else:
                coordinates_list.append(int(i))
        except ValueError:
            print("You should enter numbers!")
    for index, value in enumerate(board):
        if value == coordinates_list and (start[index] == " " or start[index] == "_"):
            start[index] = turn
            print(f"---------\n| {start[0]} {start[1]} {start[2]} |\n| {start[3]} {start[4]} {start[5]} |\n"
                  f"| {start[6]} {start[7]} {start[8]} |\n---------")
            break
        elif value == coordinates_list and (start[index] == "X" or start[index] == "O"):
            print("This cell is occupied! Choose another one!")
            player_turn = not player_turn
            break
    if " " not in start:
        print("Draw")
        game_loop = False
    for i in range(0, 9, 3):
        if start[i] == start[i + 1] == start[i + 2] != " ":
            win.append(start[i])

    for i in range(0, 3):
        if start[i] == start[i + 3] == start[i + 6] != " ":
            win.append(start[i])

    if start[0] == start[4] == start[8] != " " or start[2] == start[4] == start[6] != " ":
        win.append(start[4])

    if len(win) == 1:
        print(win[0], "wins")
        game_loop = False
    player_turn = not player_turn
