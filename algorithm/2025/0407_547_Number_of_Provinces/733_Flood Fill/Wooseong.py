'''
2 1 2
1 2 0
2 0 2
'''

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 사용할 변수들 초기화
        # m, n : image size
        # visited : 방문처리
        # target : image[sr][sc]의 값 == 변경 대상의 픽셀값
        m = len(image)  
        n = len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        target = image[sr][sc]

        # 자기 자신 먼저 바꿔놓고
        image[sr][sc] = color

        # queue에 넣고 돌리기
        queue = deque([(sr, sc)])
        while queue:
            # 하나 뽑아서
            cr, cc = queue.popleft()
            # 상, 하, 좌, 우의 이웃 탐색
            for i, j in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                # index 넘어가는 거 방지
                if ((cr + i) >= m) or ((cc + j) >= n) or ((cr + i) < 0) or ((cc + j) < 0):
                    continue
                
                # 이웃이 방문한 적 없고 변경 대상인가?
                if not visited[cr + i][cc + j] and image[cr + i][cc + j] == target:
                    image[cr + i][cc + j] = color  # inplace
                    queue.append((cr + i, cc + j))
                    visited[cr + i][cc + j] = True
        
        # inplace 처리 끝났으니까 return
        return image
