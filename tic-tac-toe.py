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


    drawgrid(dict)

    posx=input("x's turn to choose a square (1-9): ")
    if posx=="1":
        dict["pos1"]="x"
    elif posx=="2":
        dict["pos2"]="x"
    elif posx=="3":
        dict["pos3"]="x"
    elif posx=="4":
        dict["pos4"]="x"
    elif posx=="5":
        dict["pos5"]="x";
    elif posx=="6":
        dict["pos6"]="x"
    elif posx=="7":
        dict["pos7"]="x";
    elif posx=="8":
        dict["pos8"]="x"
    elif posx=="9":
        dict["pos9"]="x"
    drawgrid(dict)





def drawgrid(dict):
    print(dict["pos1"] + " | " + dict["pos2"] + " | " + dict["pos3"])
    print("- + - + -")
    print(dict["pos4"] + " | " + dict["pos5"] + " | " + dict["pos6"])
    print("- + - + -")
    print(dict["pos7"] + " | " + dict["pos8"] + " | " + dict["pos9"])


    main()