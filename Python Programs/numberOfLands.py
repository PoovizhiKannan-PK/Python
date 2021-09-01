class countIslands:
    
    def __init__(self):
        self.maps = [[1,1,0,0,0],
                    [1,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,1]]
        self.numberOfIsland( 4, 5)

    def numberOfIsland(self, rows, cols):
        count = 0
        for i in range(rows):
            for j in range(cols):
                if(self.maps[i][j] ==1):
                    count += 1
                    self.linkIsland( i, j, rows, cols)
        print(count)

    def linkIsland(self, i, j, rows, cols):
        if (i < 0 or i >= rows or j < 0 or j >= cols or self.maps[i][j] == 0):
            return
        else:
            self.maps[i][j] = 0
            self.linkIsland(i+1, j, rows, cols)
            self.linkIsland(i, j+1, rows, cols)
            self.linkIsland(i-1, j, rows, cols)
            self.linkIsland(i, j-1, rows, cols)

g = countIslands()