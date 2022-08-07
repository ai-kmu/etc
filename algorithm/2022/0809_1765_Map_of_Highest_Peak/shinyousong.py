#시간초과
class Solution:
    def upLand(self, level):
        temp = 0
        len_row = len(self.isWater)
        len_cul = len(self.isWater[0])
        for i in range(len_row):
            for j in range(len_cul):
                if self.isWater[i][j] == level\
                and (i - 1 < 0 or self.isWater[i-1][j] >= level)\
                and (j - 1 < 0 or self.isWater[i][j-1] >= level)\
                and (i + 1 >= len_row or self.isWater[i+1][j] >= level)\
                and (j + 1 >= len_cul or self.isWater[i][j+1] >= level):
                    self.isWater[i][j] = level + 1
                    temp = 1
        return temp    
    
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #전부 0, 1의 높이 표현 매트릭스로 만든다
        self.isWater = isWater
        for lst in self.isWater:
            for idx in range(len(lst)):
                if lst[idx] == 1:
                    lst[idx] = 0
                else:
                    lst[idx] = 1
        
        #매트릭스를 돌며 수렴할때까지 높이를 올린다
        level = 1
        temp = 1
        while temp == 1:
            temp = self.upLand(level)
            level += 1
        return self.isWater
