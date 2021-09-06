# For a given matrix, rotate it by 90 degree


def rotateMatrix(matrix, r, c):
    #First transpose the matrix
    for i in range(r):
        for j in range(i, c):
            if(i!=j):
                matrix[i][j] = matrix[i][j] + matrix[j][i]
                matrix[j][i] = matrix[i][j] - matrix[j][i]
                matrix[i][j] = matrix[i][j] - matrix[j][i]
    # Then swap first and last column and so on...        
    for i in range(r):
        for j in range(int(c/2)):
            matrix[i][j] = matrix[i][j] + matrix[i][c-j-1]
            matrix[i][c-j-1] = matrix[i][j] - matrix[i][c-j-1]
            matrix[i][j] = matrix[i][j] - matrix[i][c-j-1]
    
    print(matrix)


#Row and Column are same for this problem
matrix = []
r = int(input("Enter number of Rows: "))
c = int(input("Enter number of columns: "))

for i in range(r):
    col = []
    for j in range(c):
        col.append(int(input("input"+ str(i)+ "th row values: " )))
    matrix.append(col)

matrix = rotateMatrix(matrix, r, c)