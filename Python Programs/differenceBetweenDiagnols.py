# FOr a given square matrix, find the absolute difference bet sum of its diagonals.

lst = [[1,2,3],
       [4,5,6],
       [7,8,10]]

diagonalSum = 0

for i in range(len(lst[0])):
    diagonalSum += lst[i][i]

for i in range(len(lst[0])):
    diagonalSum -= lst[i][len(lst[0])-1-i]
  
if diagonalSum < 0:
    diagonalSum *= -1

print(diagonalSum)    