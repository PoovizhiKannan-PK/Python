
def spiralMatrix(mat):
    rowBegin = 0
    rowEnd = len(mat)-1
    columnBegin = 0
    columnEnd = len(mat[0])-1

    while(rowBegin <= rowEnd and columnBegin <= columnEnd):
        for i in range(columnBegin, columnEnd+1):
            print(mat[rowBegin][i])
        rowBegin += 1
        for i in range(rowBegin, rowEnd+1):
            print(mat[i][columnEnd])
        columnEnd -= 1
        if(rowBegin <= rowEnd):
            for i in range(columnEnd, columnBegin-1, -1):
                print(mat[rowEnd][i])
        rowEnd -= 1
        if(columnBegin <= columnEnd):
            for i in range(rowEnd, rowBegin-1, -1):
                print(mat[i][columnBegin])
        columnBegin +=1

mat = []

row = int(input("Enter number of rows"))
col = int(input("Enter number of column"))

for i in range(row):
    column = []
    for i in range(col):
        column.append(int(input("Enter"+str(i)+"row elements")))
    mat.append(column)

spiralMatrix(mat)