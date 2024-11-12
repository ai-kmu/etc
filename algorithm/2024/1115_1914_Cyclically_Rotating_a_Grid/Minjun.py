# 풀이 봤음. 젠장
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # 레이어들을 추출하는 함수
        def extract_layer(layer_num):
            layer = []
            for j in range(layer_num, n - layer_num):  # 상단 가로
                layer.append(grid[layer_num][j])
            for i in range(layer_num + 1, m - layer_num):  # 오른쪽 세로
                layer.append(grid[i][n - layer_num - 1])
            for j in range(n - layer_num - 2, layer_num - 1, -1):  # 하단 가로
                layer.append(grid[m - layer_num - 1][j])
            for i in range(m - layer_num - 2, layer_num, -1):  # 왼쪽 세로
                layer.append(grid[i][layer_num])
            return layer

        # 레이어를 다시 그리드에 넣는 함수
        def insert_layer(layer_num, layer):
            idx = 0
            for j in range(layer_num, n - layer_num):  # 상단 가로
                grid[layer_num][j] = layer[idx]
                idx += 1
            for i in range(layer_num + 1, m - layer_num):  # 오른쪽 세로
                grid[i][n - layer_num - 1] = layer[idx]
                idx += 1
            for j in range(n - layer_num - 2, layer_num - 1, -1):  # 하단 가로
                grid[m - layer_num - 1][j] = layer[idx]
                idx += 1
            for i in range(m - layer_num - 2, layer_num, -1):  # 왼쪽 세로
                grid[i][layer_num] = layer[idx]
                idx += 1

        # 각 레이어에 대해 k번 회전 후 다시 삽입
        num_layers = min(m, n) // 2
        for layer_num in range(num_layers):
            layer = extract_layer(layer_num)
            actual_k = k % len(layer)  # 실제 필요한 회전 수
            rotated_layer = layer[actual_k:] + layer[:actual_k]  # 회전된 레이어
            insert_layer(layer_num, rotated_layer)

        return grid
