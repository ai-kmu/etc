# 이게 뭐노!!!! 답 봐버렸어요 리뷰 안해줘도 됨


class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 레이러 추출
        def extract_layer(grid, layer):
            
            m, n = len(grid), len(grid[0])
            elements = []

            # 위쪽 행
            for i in range(layer, n - layer):
                elements.append(grid[layer][i])
            # 오른쪽 열
            for i in range(layer + 1, m - layer):
                elements.append(grid[i][n - layer - 1])
            # 아래쪽 행
            for i in range(n - layer - 2, layer - 1, -1):
                elements.append(grid[m - layer - 1][i])
            # 왼쪽 열
            for i in range(m - layer - 2, layer, -1):
                elements.append(grid[i][layer])

            return elements
        # 추출한 요소를 레이어에 삽입
        def insert_layer(grid, layer, elements):
            m, n = len(grid), len(grid[0])
            idx = 0

            # 위쪽 행
            for i in range(layer, n - layer):
                grid[layer][i] = elements[idx]
                idx += 1
            # 오른쪽 열
            for i in range(layer + 1, m - layer):
                grid[i][n - layer - 1] = elements[idx]
                idx += 1
            # 아래쪽 행
            for i in range(n - layer - 2, layer - 1, -1):
                grid[m - layer - 1][i] = elements[idx]
                idx += 1
            # 왼쪽 열
            for i in range(m - layer - 2, layer, -1):
                grid[i][layer] = elements[idx]
                idx += 1

        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elements = extract_layer(grid, layer)
            # 회전 수를 요소의 길이로 나눈 나머지 계산
            rotation = k % len(elements) 
            elements = elements[rotation:] + elements[:rotation]  
            insert_layer(grid, layer, elements) 

        return grid
