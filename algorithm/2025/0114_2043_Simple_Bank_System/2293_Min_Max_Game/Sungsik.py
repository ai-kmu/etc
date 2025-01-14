class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            new_nums = []
            is_min = True
            for n1, n2 in zip(nums[::2], nums[1::2]):
                new_nums.append(min(n1, n2) if is_min else max(n1, n2))
                is_min = not is_min
            nums = new_nums.copy()
        return nums[0]
