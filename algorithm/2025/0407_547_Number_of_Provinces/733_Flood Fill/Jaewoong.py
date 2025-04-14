from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        m, n = len(image), len(image[0])
        coor = deque()
        coor.append((sr, sc))

        while coor:
            print(coor)
            r, c = coor.popleft()
            if image[r][c] == original_color:
                image[r][c] = color
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        coor.append((nr, nc))


        return image
