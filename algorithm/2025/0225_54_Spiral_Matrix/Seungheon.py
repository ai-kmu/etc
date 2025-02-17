class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        answer = []
        position_set = set()
        cur_i, cur_j = 0, 0

        move_idx = 0
        move_list = [[0,1],[1,0],[0,-1],[-1,0]]

        # 모두 돌때까지
        while len(position_set) < len(matrix) * len(matrix[0]):
            
            # 현재 위치 저장
            position_set.add((cur_i, cur_j))
            answer.append(matrix[cur_i][cur_j])

            # 이동
            next_i = cur_i + move_list[move_idx % 4][0]
            next_j = cur_j + move_list[move_idx % 4][1]

            # 방문한적 있거나 밖으로 나가면
            if (next_i, next_j) in position_set or next_i < 0 or next_i >= len(matrix) or next_j < 0 or next_j >= len(matrix[0]):
                move_idx += 1 # 방향 전환
                cur_i += move_list[move_idx % 4][0]
                cur_j += move_list[move_idx % 4][1]
            else:
                cur_i, cur_j = next_i, next_j
                
        return answer
            

            
