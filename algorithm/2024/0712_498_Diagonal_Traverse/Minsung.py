class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ascending = True  # True for brown direction, False for yellow direction
        i = j = 0  # current position: i for row, j for column
        ans = list()  
        for t in range(len(mat) * len(mat[0])):  
            ans.append(mat[i][j])
            if ascending:  # for brown direction
                i -= 1  
                j += 1
                if not self.safe(mat, i, j):  # 방향 전환
                    i += 1
                    if not self.safe(mat, i, j):  
                        i += 1
                        j -= 1
                    ascending = False
            else:  # for yellow direction
                i += 1
                j -= 1
                if not self.safe(mat, i, j):  # 방향 전환
                    j += 1
                    if not self.safe(mat, i, j):
                        i -= 1
                        j += 1
                    ascending = True
        return ans
    
    def safe(self, mat, i, j):  # 현재 위치가 matrix boundary 내에 있는 지 check
        return True if i>=0 and i<len(mat) and j>=0 and j<len(mat[0]) else False
