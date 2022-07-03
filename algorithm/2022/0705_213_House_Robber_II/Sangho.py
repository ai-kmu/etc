class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        # 첫번째 집 안털었을 때
        NoFirst = [0, nums[1]]
        # 첫번째 집 털었을 때
        YesFirst = [nums[0], nums[0]]
        
        for i in range(2, len(nums)):
            # case1) 전전집에서 넘기고 현재 집에서 훔침
            # case2) 바로 전 집에서 넘기고 현재 집에서는 안훔침
            NoFirst.append(max(NoFirst[-2] + nums[i], NoFirst[-1]))
            YesFirst.append(max(YesFirst[-2] + nums[i], YesFirst[-1]))
        
        # maximum value 리턴:
        # case1) 첫집에서 안털고 아무렇게나
        # case2) 첫집에서 털고 마지막집 포함x
        # case3) 마지막집
        return max(NoFirst[-1], YesFirst[-2], nums[-1])
