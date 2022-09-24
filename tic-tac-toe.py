dict = {
    "pos1": "1", 
    "pos2": "2", 
    "pos3": "3",
    "pos4": "4",
    "pos5": "5",
    "pos6": "6",
    "pos7": "7",
    "pos8": "8",
    "pos9": "9",
}
 

def main():   
    player = next_player("")
    board = drawgrid(dict)
    while not (winner(board) or tie(board)):
        drawgrid(board)
        move(player, board)
        player = next_player(player)
    drawgrid(board)
    print("Thanks for playing!")

def drawgrid(dict):
    print(dict["pos1"] + " | " + dict["pos2"] + " | " + dict["pos3"])
    print("- + - + -")
    print(dict["pos4"] + " | " + dict["pos5"] + " | " + dict["pos6"])
    print("- + - + -")
    print(dict["pos7"] + " | " + dict["pos8"] + " | " + dict["pos9"])

def tie(dict):
    for i in range(dict[i]):
        if dict[i] != "x" and dict[i] != "o":
            return False
    return True 

def winner(board):
    return (dict["pos1"] == dict["pos2"] == dict["pos3"] or
            dict["pos4"] == dict["pos5"] == dict["pos6"] or
            dict["pos7"] == dict["pos8"] == dict["pos9"] or
            dict["pos1"] == dict["pos4"] == dict["pos7"] or
            dict["pos2"] == dict["pos5"] == dict["pos8"] or
            dict["pos3"] == dict["pos6"] == dict["pos9"] or
            dict["pos1"] == dict["pos5"] == dict["pos9"] or
            dict["pos3"] == dict["pos5"] == dict["pos7"])


def move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"







if __name__ == "__main__":
    main()