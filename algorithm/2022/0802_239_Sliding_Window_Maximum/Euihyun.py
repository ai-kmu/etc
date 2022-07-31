# 타임out..
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        ans = []
        n = len(nums)
        # 슬라이딩 방식으로 정답값 채워넣기 위해서 n-k+1 개씩 사용
        # 슬라이딩 안에서 맥스값만 정답에 append
        for i in range(n-k+1):
            ans.append(max(nums[i:i+k]))
            
        return ans
        
