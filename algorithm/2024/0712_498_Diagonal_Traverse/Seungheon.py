class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        answer = []

        right_up = (-1, 1)
        left_down = (1, -1)
        cur_point = (0, 0)
        
        flag = True # True = right_up, False = left_down

        # answer 이 다 찰때까지
        while len(answer) < m*n:
            answer.append(mat[cur_point[0]][cur_point[1]])
            if flag: # right_up
                next_i, next_j = cur_point[0] + right_up[0], cur_point[1] + right_up[1]
                # 넘어가면
                if next_j >= n:
                    flag = False
                    next_i, next_j = cur_point[0] + 1, cur_point[1]
                elif next_i < 0:
                    flag = False
                    next_i, next_j = cur_point[0], cur_point[1] + 1
            else: # left_down
                next_i, next_j = cur_point[0] + left_down[0], cur_point[1] + left_down[1]
                # 넘어가면
                if next_i >= m:
                    flag = True
                    next_i, next_j = cur_point[0], cur_point[1] + 1
                elif next_j < 0:
                    flag = True
                    next_i, next_j = cur_point[0] + 1, cur_point[1]

            cur_point = (next_i, next_j)

        return answer
