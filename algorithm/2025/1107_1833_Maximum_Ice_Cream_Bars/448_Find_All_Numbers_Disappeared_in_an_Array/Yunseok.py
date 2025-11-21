class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        max_val = len(nums)
        num_set = set(nums)
        nums = list(num_set)

        nums_full_list = []
        for i in range(max_val):
            nums_full_list.append(i+1)

        nums_full_set = set(nums_full_list)
        print(nums_full_set)

        for num in nums:
            if num in nums_full_set:
                nums_full_set.remove(num)
        
        # print(nums_full_set)
        return list(nums_full_set)
