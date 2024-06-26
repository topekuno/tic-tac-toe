# A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    x = int(position)
    board[x] = mark
    return


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1

def printBoard():
    # Using .copy() to create a new dictionary that doesn't reference it in memory with board
    x = board.copy()
    for k, v in x.items():
        if v == ' ':
            x[k] = str(k)
            
    print("\n")
    print(" {} | {} | {}".format(x[1],x[2],x[3]))
    print(" ---------")
    print(" {} | {} | {}".format(x[4],x[5],x[6]))
    print(" ---------")
    print(" {} | {} | {}".format(x[7],x[8],x[9]))
    print("\n")
    return


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    # Using try and except to convert string into integer if it fails it will return False
    try:
        # Converts position to integer
        x = int(position)
        # Checks if input is more than 9
        if x > 9:
            return False
        # Checks if input is less than 1
        elif x < 1:
            return False
        # Checks if board is empty at the position given
        else:
            if board[x] == ' ':
                return True
            else:
                return False
    except:
        return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    winCheck = []
    # Create an array to know which keys the player occupies
    for k, v in board.items():
        if v == player:
            winCheck.append(k)
    # Check if the elements in the array is less than 3
    if len(winCheck) < 3:
        return False
    # Iterate thru all possible combinations in winCheck array:
    else:
        n = len(winCheck)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # Check if the winCheck contains the winnig combinations
                    for l in winCombinations:
                        if winCheck[i] == l[0] and winCheck[j] == l[1] and winCheck[k] == l[2]:
                            return True
        # If there is no winning combinations return False
        return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    k = 0
    for i in board.values():
        if i == 'X' or i == 'O':
            k += 1

    if k == 9:
        return True
    else:
        return False


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

# To reset the board to default after restart
def resetBoard():
    for key in board.keys():
        board[key] = ' '

# One big while loop for restart purposes 
gameRestart = True
while gameRestart == True:

    gameEnded = False
    currentTurnPlayer = 'X'
    resetBoard()

    # entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')

    # TODO: Complete the game play logic below
    # You could reference the following flow
    # 1. Ask for user input and validate the input
    # 2. Update the board
    # 3. Check win or tie situation
    # 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        if validateMove(move) == True:
            markBoard(move,currentTurnPlayer)
            printBoard()
        else:
            print("Invalid input!")
            continue

        # Check if player won or a tie
        if checkWin(currentTurnPlayer) == True:
            print("Player {} has won!".format(currentTurnPlayer))
            gameEnded = True
        elif checkFull() == True:
            print("It's a tie!")
            gameEnded = True
        else:
            # Switch player
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            elif currentTurnPlayer == 'O':
                currentTurnPlayer = 'X'

    # Ask if the player wants to restart
    restart = input("Do you want to play again? (Y/N): ")
    if restart not in ['Y','y']:
        print("Thanks for playing!")
        gameRestart = False
        

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
