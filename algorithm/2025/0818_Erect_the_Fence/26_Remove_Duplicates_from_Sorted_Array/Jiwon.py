class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                # print(f"pre: {nums}")
                i += 1
                nums[i] = nums[j]  # 뒤는 상관없으니까? 정렬용
                # print(f"af: {nums}")

        return len(set(nums))
