class Solution:
    def queensAttacktheKing(self, queens, king):
        matrix = [[0] * 8 for _ in range(8)]
        
        for i, j in queens:
            matrix[i][j] = 1
        
        result = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
                
        for i, j in directions:
            king_i = king[0]
            king_j = king[1]
            while 0 <= king_i < 8 and 0 <= king_j < 8:
                if matrix[king_i][king_j] == 1:
                    result.append([king_i, king_j])
                    break
                king_i += i
                king_j += j
        
        return result
