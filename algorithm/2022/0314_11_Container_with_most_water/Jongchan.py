class Solution:
    def maxArea(self, height: List[int]) -> int:
      
        answer=0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                tmp = min(height[i],height[j])*abs(i-j)
                if tmp>answer:
                    answer=tmp
        
        return answer
