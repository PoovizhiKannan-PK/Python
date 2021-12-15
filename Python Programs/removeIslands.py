
def checkup(matrix, i, j):
    rows = len(matrix)
    while(i >= 0):
        if matrix[i][j] == 0:
            return True
        i -= 1
    return False


def checkdown(matrix, i, j):
    rows = len(matrix)
    while(i < rows):
        if matrix[i][j] == 0:
            return True
        i += 1
    return False


def checkleft(matrix, i, j):
    col = len(matrix[i])
    while(j >= 0):
        if matrix[i][j] == 0:
            return True
        else:
            break
        j -= 1
    return False


def checkright(matrix, i, j):
    col = len(matrix[i])
    while(j < col):
        if matrix[i][j] == 0:
            return True
        else:
            break
        j += 1
    return False


def removeIslands(matrix):
    rows = len(matrix)
    col = len(matrix[1])
    for i in range(1, rows-1):
        for j in range(1, col-1):
            if((checkup(matrix, i-1, j)) and (checkdown(matrix, i+1, j)) and (checkleft(matrix, i, j-1)) and (checkright(matrix, i, j+1))):
                matrix[i][j] = 0

    return matrix


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

mat = removeIslands(matrix)

for row in mat:
    print(row)
