# Time limit

class Solution(object):
    
    def calcPeak(self, ans, r, c, cnt):
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                # 거리 계산 
                temp = abs(r - i) + abs(c - j)
                # 첫번째 일때는 값이 다 0으로 초기화 되어있기 때문에 바로 temp값을 넣어준다
                # 그 외의 경우에는 더 작은 값을 넣어준다
                if cnt == 1 or temp < ans[i][j]:
                    ans[i][j] = temp

        return ans
    
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [[0 for j in range(len(isWater[i]))] for i in range(len(isWater))]
        cnt = 0
        
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j]:
                    cnt += 1
                    ans = self.calcPeak(ans, i, j, cnt)
        
        return ans
    
    
