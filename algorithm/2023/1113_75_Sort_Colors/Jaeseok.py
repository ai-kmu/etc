class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0의 갯수와 1의 갯수만 세면 됨
        zeros, ones = 0, 0
        for i, v in enumerate(nums):
            if nums[i] == 0:
                zeros += 1 
            elif nums[i] == 1:
                ones += 1 

        # 다시 순회하면서 0의 갯수가 남아있으면 계속 0으로
        # 1의 갯수가 남아있으면 1로 바꿔줌
        # 둘다 아니면 2로 나머지 채워줌
        for i, v in enumerate(nums):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
            elif zeros == 0 and ones != 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
              
