class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = range(1, len(nums) + 1)  # 탐색 대상
        nums = set(nums)  # 탐색 O(1)로 줄이기
        answer = []
        for i in x:
            # 없는 거 append해서 return
            if i not in nums:
                answer.append(i)
        
        return answer
