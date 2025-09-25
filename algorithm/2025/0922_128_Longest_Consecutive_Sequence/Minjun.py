class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 빈 리스트 처리
        if not nums:
            return 0
        # 중복을 제거하라 !!!
        a = set(nums)
        now = 0
        longest = 1

        for i in a: # O(n)
            # 이어질 수 있는 최소 수에서 시작함.
            # 중간 수는 생략.
            if i-1 not in a: # O(1)
                now = 0
                while i in a: # O(1)
                    now += 1
                    i += 1
            if longest < now:
                longest = now
        return longest
                
