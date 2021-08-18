# BFS로 품

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cases = [[-1,0],[1,0],[0,-1],[0,1]]
        len_y = len(mat)
        len_x = len(mat[0])
        
        #queue에 우선 mat=0인 index를 저장해둠
        queue = []
        for y in range(len_y):
            for x in range(len_x):
                if mat[y][x] == 0:
                    queue.append([0,y,x])
                else:
                    mat[y][x] = -1
                    
        # mat=0인 index를 시작점으로 bfs 시작
        while(queue):
            dist, y,x = queue.pop(0)
            for c in cases:
                y_, x_ = y+c[0], x+c[1]
                if 0<= y_ < len_y and 0<=x_<len_x and mat[y_][x_] == -1:
                    mat[y_][x_] = dist+1
                    queue.append([dist+1, y_, x_])
                    
        return mat    
        
