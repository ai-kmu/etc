from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        tmp_color = image[sr][sc]

        m, n = len(image), len(image[0])
        
        queue = deque([(sr, sc)])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            r, c = queue.popleft()

            image[r][c] = color

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n and image[new_r][new_c] == tmp_color:
                    queue.append((new_r, new_c))
        return image
