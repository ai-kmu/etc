class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        n, m = len(image), len(image[0])
        start_color = image[sr][sc]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or image[x][y] != start_color or image[x][y] == color:
                return
            
            image[x][y] = color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        dfs(sr, sc)
        return image


            
