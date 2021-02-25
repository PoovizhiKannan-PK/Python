
def printSpiral(a, right, bottom):
    top = 0
    left = 0
    direction = 0
    while(top <= bottom and left <=right):
        if direction == 0:
            for i in range(left, right):
                print(a[top][i], end = " ")
            top += 1
        elif direction == 1:
            for i in range(top, bottom):
                print(a[i][right-1], end = " ")
            right -= 1
        elif direction == 2:
            for i in range(right-1, left-1, -1):
                print(a[bottom-1][i], end = " ")
            bottom -= 1
        elif direction == 3:
            for i in range(bottom-1, top-1, -1):
                print(a[i][left], end = " ")
            left += 1
        direction = (direction+1)%4



a = [[1,2,3,4],
     [7,8,9,5],
     [13,14,15,6]]

printSpiral(a, 4, 3)