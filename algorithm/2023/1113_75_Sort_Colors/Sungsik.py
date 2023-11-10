class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # one-pass algorithm은 방식이 안떠올라 twe-pass algorithm으로 구현했습니다
        count = [0] * 3
        
        # 0, 1, 2 개수 세기
        for n in nums:
            count[n] += 1
        
        # 개수만큼 replace
        for i, n in enumerate([0] * count[0] + [1] * count[1] + [2] * count[2]):
            nums[i] = n
        
