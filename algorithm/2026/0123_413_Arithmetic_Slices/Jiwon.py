class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        lenNums = len(nums)
        if lenNums < 3:
            return 0
        
        ans = 0
        cnt = 1
        # 최소 세 개의 요소로 구성
        for i in range(2, lenNums):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans += cnt  # 앞에서 센 거 제외하고 새로 생긴 애들
                cnt += 1
            else:
                cnt = 1  # 처음부터 세야 함
        return ans
