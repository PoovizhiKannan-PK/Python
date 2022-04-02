
def ifWon(board):
    # Horizontal
    for row in board:
        if row[0] != 0 and row.count(row[0]) == 0:
            return True
    # Vertical
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check[0] != 0 and check.count(check[0]) == 3:
            return True

    # diagonal
    if board[0][0] != 0:
        check = []
        for row in range(len(board)):
            check.append(board[row][row])
        if check.count(check[0]) == 3:
            return True

    if board[0][len(board[0])-1] != 0:
        check = []
        for row in range(len(board)):
            check.append(board[row][len(board[0])-1-row])
        if check.count(check[0]) == 3:
            return True

    return False


def gamePlay(board, player, visit):
    while True:
        while True:
            row = int(input(f"Player {player} Choose a row among 0, 1, 2 \n"))
            if row not in [0, 1, 2]:
                print('Choose a valid row')
            else:
                break
        while True:
            col = int(
                input(f'Player {player} Choose a column among 0, 1, 2 \n'))
            if col not in [0, 1, 2]:
                print('Choose a valid column')
            else:
                break
        if (row, col) in visit:
            print("Selected row, col has already been played")
        else:
            visit.add((row, col))
            break

    board[row][col] = player
    print("   0  1  2")
    for count, row in enumerate(board):
        print(count, row)
    return ifWon(board)


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
gameWon = False
players = [1, 2]
currPlayer = 2
visit = set()
print("   0  1  2")
for count, row in enumerate(board):
    print(count, row)

while not gameWon:
    if currPlayer == 2:
        currPlayer = 1
    else:
        currPlayer = 2

    gameWon = gamePlay(board, currPlayer, visit)
    if gameWon:
        print(f"Player {currPlayer} Won")
    if len(visit) == (len(board) * len(board[0])):
        print("Game Draw")
        break
