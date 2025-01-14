class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while True:
            if len(nums) == 1:
                return nums[0]
            new_nums = []
            is_min = True
            for n1, n2 in zip(nums[::2], nums[1::2]):
                new_nums.append(min(n1, n2) if is_min else max(n1, n2))
                is_min = not is_min
            nums = new_nums.copy()
