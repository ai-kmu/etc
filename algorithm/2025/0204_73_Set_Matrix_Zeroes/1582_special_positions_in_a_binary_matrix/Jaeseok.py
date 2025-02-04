class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        answer = 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    flag = False
                    for k in range(m):
                        if mat[k][j] == 1 and k != i:
                            flag = True
                    for l in range(n):
                        if mat[i][l] == 1 and l != j:
                            flag = True
                    if flag == False:
                        answer += 1
        
        return answer


# 더 나은 풀이
from collections import Counter

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        answer = 0
        m, n = len(mat), len(mat[0])
        rowsum = [0] * m
        colsum = [0] * n
        for i in range(m):
            rowsum[i] = mat[i].count(1)

        for j in range(n):
            colsum[j] = Counter(row[j] for row in mat)[1]
            
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowsum[i] == 1 and colsum[j] == 1:
                    answer += 1
                    
        return answer
