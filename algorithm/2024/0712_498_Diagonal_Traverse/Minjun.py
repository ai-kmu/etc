# 풀이 실패

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = mat[0]
        f = 2
        for _ in range(1, len(mat)):
            for i in mat[_]:
                if f >= len(answer):
                    answer.append(i)
                else:
                    answer = answer[:f].append(i)
                f += 2
        return answer
            
