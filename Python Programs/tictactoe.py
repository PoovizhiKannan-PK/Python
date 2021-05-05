import itertools

def win(game_board):
    for row in game_board:
        if row[0] != 0 and row.count(row[0]) == len(row):
            print("Player {row[0]} won")
            return True
    
    
    for col in range(len(game_board)):
        check = []
        for row in game_board:
            check.append(row[col])
        if check[0] != 0 and check.count(check[0]) == len(check):
            print("Player {row[0]} won")
            return True
    
    # \ diagnol
    check = []
    for row in range(len(game_board)):
        check.append(game_board[row][row])
    if check[0] != 0 and check.count(check[0]) == len(check):
        print("Player {check[0]} won")
        return True

    # / diagnol
    check = []
    for ids, rev_id in enumerate(reversed(range(len(game_board)))):
        check.append(game_board[ids][rev_id])
    if check[0] != 0 and check.count(check[0]) == len(check):
        print("Player {check[0]} won")
        return True

    return False


def game_play(game_board, player=0, row=0, coloumn=0):
    try:
        game_board[row][coloumn] = player
        print(" 0 1 2")
        for count, row in enumerate(game_board):
            print(count, row)
        ifWon = win(game_board)
        return ifWon
    except IndexError:
        print("For row and coloumn select numbers amoung 0, 1 and 2")
        return False
    except Exception as e:
        print("Error: {}".format(e))
        return False        



game_won = False
game_board = [[0,0,0],
              [0,0,0],
              [0,0,0]]
players = [1,2]
player_cycle = itertools.cycle(players)

print(" 0 1 2")
for count, row in enumerate(game_board):
    print(count, row)
while not game_won:
    player = next(player_cycle)
    print('Current Player: ', player)
    row = int(input('Input row choice: '))
    coloumn = int(input('Input column choice: '))
    game_won = game_play(game_board, player, row, coloumn)