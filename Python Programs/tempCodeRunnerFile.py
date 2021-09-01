
    def numberOfIsland(self, rows, cols):
        count = 0
        for i in range(rows):
            for j in range(cols):
                if(self.maps[i][j] ==1):
                    count += 1
                    self.linkIsland(i, j, row