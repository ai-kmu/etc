class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        answer = []
        for i in range(len(nums)):
            i += 1
            if i not in nums_set:
                answer.append(i)

        return answer
