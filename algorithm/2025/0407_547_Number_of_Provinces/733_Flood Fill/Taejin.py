class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        target = image[sr][sc]

        def bfs(x, y):
            nonlocal image, visited, target
            if not visited[x][y] and (image[x][y] == target):
                visited[x][y] = True
                image[x][y] = color

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if (0 <= new_x < len(image)) and (0 <= new_y < len(image[0])):
                        bfs(new_x, new_y)

        bfs(sr, sc)
        return image


        
