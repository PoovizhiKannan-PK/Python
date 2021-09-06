# For a given int n = 3, construct a matrix of size n^2 = 3x3, with values 1,2....,n^2(9)


n = 4
count = 1
rowStart = 0
rowEnd = n-1
colStart = 0
colEnd = n-1
mat = []
for i in range(n):
    col = []
    for j in range(n):
        col.append(0)
    mat.append(col)

print(mat)

while(rowStart <= rowEnd and colStart <= colEnd):
    for i in range(colStart, colEnd+1):
        mat[rowStart][i] = count
        count += 1
    rowStart += 1

    for i in range(rowStart, rowEnd+1):
        mat[i][colEnd] = count
        count += 1
    colEnd -= 1

    for i in range(colEnd, colStart-1, -1):
        mat[rowEnd][i] = count
        count += 1
    rowEnd -= 1

    for i in range(rowEnd, rowStart-1, -1):
        mat[i][colStart] = count
        count += 1
    colStart += 1

print(mat)

