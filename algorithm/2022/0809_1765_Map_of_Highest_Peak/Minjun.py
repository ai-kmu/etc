# 오답
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        hmap = [[1 for i in range(len(isWater))] for j in range(len(isWater[0]))]
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    hmap[i][j] = 0
        for i, k in enumerate(hmap):
            print(i, k)
            for j in k:
                print(j)
                
    def bfs(i, j):
        k = hmap[i][j]
        if hmap[i-1][j] - :
        
        
