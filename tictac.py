def main():
    """ We're going to try to make a tic tac toe game.
        We will draw a board, take numbers inputs.
    """
    #Initialize variables
    playArray = list(range(1, 10))
    while True:
        turn = 0
        for vals in playArray:
            if vals == "X" or vals == "O":
                turn = turn + 1
        playerChar = checkPlayer(turn)
        printBoard(playArray)
        print("Player {}, where you would like to play?".format(playerChar))
        userInput = input()
        if userInput == "q" or userInput == "Q":
            return
        action = validateInput(userInput, playArray)
        if action != 0:
            playArray[action - 1] = playerChar
            turn = turn + 1
        print(turn)
        if checkForEnd(playArray, playerChar):
            print("Congratulations!!!!! YOU WIN!!!! \n PLAYER {}".format(
                playerChar))
            break
        if turn == 9:
            print("Cats game, tie")
            break


def checkForEnd(playArray, player):
    win = False
    if playArray[6] == playArray[7] == playArray[8] == player:
        win = True
    elif playArray[6] == playArray[4] == playArray[2] == player:
        win = True
    elif playArray[6] == playArray[3] == playArray[0] == player:
        win = True
    elif playArray[7] == playArray[4] == playArray[1] == player:
        win = True
    elif playArray[8] == playArray[4] == playArray[0] == player:
        win = True
    elif playArray[8] == playArray[5] == playArray[2] == player:
        win = True
    elif playArray[3] == playArray[4] == playArray[5] == player:
        win = True
    elif playArray[0] == playArray[1] == playArray[2] == player:
        win = True
    return win


def checkPlayer(turnCount):
    if turnCount % 2 == 0:
        return "X"
    else:
        return "O"


def printBoard(playArray):
    print("{}|{}|{}".format(playArray[6], playArray[7], playArray[8]))
    print("-----")
    print("{}|{}|{}".format(playArray[3], playArray[4], playArray[5]))
    print("-----")
    print("{}|{}|{}".format(playArray[0], playArray[1], playArray[2]))


def validateInput(inputVal, playArray):
    try:
        int(inputVal)
    except:
        print("Not a valid input.  Try again")
        return 0
    intVal = int(inputVal)
    if intVal > 9 or intVal < 1:
        print("Not a valid input.  Please enter a value between 1 and 9")
        return 0
    elif playArray[intVal - 1] == "X" or playArray[intVal - 1] == "O":
        print(
            "Not a valid input.  Please enter an available spot on the play board"
        )
        return 0
    else:
        return intVal


if __name__ == "__main__":
    main()
