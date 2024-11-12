class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.row, self.col = len(grid), len(grid[0])
        layer = self.grid_to_layer(grid)  # grid 형태를 layer로 변환
        layer = self.rotate_layer(layer, k)  # rotation 진행
        return self.layer_to_grid(layer)  # layer 형태를 grid로 변환

    def rotate_layer(self, layer, k):
        for i in range(len(layer)):
            cur_layer = layer[i]
            step = k % len(cur_layer)  # 각 layer 길이로 mod
            concatanated_cur_layer = cur_layer + cur_layer 
            start_value = concatanated_cur_layer[0]
            for j in range(len(cur_layer)):
                concatanated_cur_layer[j] = concatanated_cur_layer[j+step]
            layer[i] = concatanated_cur_layer[:len(cur_layer)] 
        return layer

    def grid_to_layer(self, grid):
        n_layers = min(self.row, self.col) // 2  # grid의 layer 수
        layer = [[] for _ in range(n_layers)]
        for cur_layer in range(n_layers):
            start_point = (cur_layer, cur_layer)
            end_point = (self.row-cur_layer-1, self.col-cur_layer-1)  # layer 좌측 상단 지점
            cur_point = list(start_point)  # layer 우측 하단 지점
            '''
            Step 1:
                start_x, start_y  ->  start_x, end_y
            Step 2:
                start_x, end_y  ->  end_x, end_y
            Step 3:
                end_x, end_y  ->  end_x, start_y
            Step 4:
                end_x, start_y  ->  start_x, start_y
            '''
            while cur_point[1] != end_point[1]:
                layer[cur_layer].append(grid[cur_point[0]][cur_point[1]])
                cur_point[1] += 1
            while cur_point[0] != end_point[0]:
                layer[cur_layer].append(grid[cur_point[0]][cur_point[1]])
                cur_point[0] += 1
            while cur_point[1] != start_point[1]:
                layer[cur_layer].append(grid[cur_point[0]][cur_point[1]])
                cur_point[1] -= 1
            while cur_point[0] != start_point[0]:
                layer[cur_layer].append(grid[cur_point[0]][cur_point[1]])
                cur_point[0] -= 1
        return layer
    
    def layer_to_grid(self, layer):
        grid = [[0]*self.col for _ in range(self.row)]
        for i, cur_layer in enumerate(layer):
            start_point = (i, i)
            end_point = (self.row-i-1, self.col-i-1) 
            cur_point = list(start_point)
            idx = 0  # 각 layer list의 index
            # grid_to_layer와 동일함 
            while cur_point[1] != end_point[1]:
                grid[cur_point[0]][cur_point[1]] = cur_layer[idx]
                cur_point[1] += 1
                idx += 1
            while cur_point[0] != end_point[0]:
                grid[cur_point[0]][cur_point[1]] = cur_layer[idx]
                cur_point[0] += 1
                idx += 1
            while cur_point[1] != start_point[1]:
                grid[cur_point[0]][cur_point[1]] = cur_layer[idx]
                cur_point[1] -= 1
                idx += 1
            while cur_point[0] != start_point[0]:
                grid[cur_point[0]][cur_point[1]] = cur_layer[idx]
                cur_point[0] -= 1
                idx += 1
        return grid
