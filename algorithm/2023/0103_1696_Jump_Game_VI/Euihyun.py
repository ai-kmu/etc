# 일반적인 dp로 풀었다가 타임 리밋나서 보고 공부했습니다.
# 리뷰 따로 안해주셔도 됩니다.

class Solution:
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        deq = deque()
        deq.append(0)
        dp = [0 for i in range(n)] 
        dp[0] = nums[0]
        
        for i in range(1, n):
            # dp 테이블 업데이트
            dp[i] = nums[i] + dp[deq[0]]     
            # k만큼 한바퀴를 돌았다면 deq값을 뺌
            if deq[0] < i - k + 1:
                deq.popleft()                
            
            # deq 가 비어있지 않고 새로운 값이 더 크면 다음바퀴로 넘어감
            while deq and dp[deq[-1]] < dp[i]:         
                deq.pop()                    
            # 다음 바퀴를 위해 업데이트
            deq.append(i)
            
        return dp[-1]                       
