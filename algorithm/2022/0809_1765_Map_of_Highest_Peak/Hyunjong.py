import copy
# 오답 코드, queue에 저장해서 풀면 된다고 들었지만 결국 구현 실패함
class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        d = [(-1,0),(1,0),(0,1),(0,-1)]
        q = collections.deque()
        
        dp = []
        
        for i in range(len(isWater)):
            dp.append([0] * len(isWater[0]))
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]==1:
                    dp[i][j] = 0
                    q.append([i,j,0])
        return
