class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.visited = [[False]*len(image[0]) for _ in range(len(image))]
        self.index = list()
        self.dfs(sr, sc)
        for x, y in self.index:
            self.image[x][y] = color
        return self.image
    
    def dfs(self, x, y):
        self.visited[x][y] = True
        self.index.append((x,y))
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx>=0 and tx<len(self.image) and ty>=0 and ty<len(self.image[0]):
                if self.image[tx][ty] == self.image[x][y] and self.visited[tx][ty]==False:
                    self.dfs(tx,ty)
