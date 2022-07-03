class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums 길이가 1에서 3까지는 nums에서 최대값과 같음
        if len(nums) >= 1 and len(nums) <= 3:
            return max(nums)

        else:
            # 각 두 dp별 초기 인덱스 0과 1에서의 값 선언
            dp_even = [0 for _ in range(len(nums))] # index 0부터 들르는 경우
            dp_odd = [0 for _ in range(len(nums))] # index 1부터 들르는 경우
            
            # index 0부터 들르는 경우 dp의 0과 1에서의 값은 nums[0]으로 초기화
            dp_even[0] = nums[0]
            dp_even[1] = nums[0]
            
            # index 1부터 들르는 경우 dp의 0과 1에서의 값은 각각 0과 nums[1]으로 초기화
            dp_odd[0] = 0
            dp_odd[1] = nums[1]
            
            # dp 수행
            for i in range(2, len(nums)):
                # 첫번째 집과 마지막 집 둘 다 접근할 수 없으므로 첫번째 집부터 들르는 경우는 마지막 인덱스 접근 안함
                if i != len(nums)-1:
                    dp_even[i] = max(dp_even[i-1], dp_even[i-2] + nums[i])
                dp_odd[i] = max(dp_odd[i-1], dp_odd[i-2] + nums[i])
                
            return max(max(dp_even), max(dp_odd))
