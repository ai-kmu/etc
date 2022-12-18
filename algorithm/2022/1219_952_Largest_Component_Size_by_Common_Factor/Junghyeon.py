'''
부모가 두개인 경우에 해결 x 
'''

from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def is_disjoint(a, b):
            i = 2
            min_num = min(a, b)
            while i <= min_num:
                if a % i == 0 and b % i == 0:
                    return False
                i += 1
            return True

        def find(parent, x, cnt):
            if parent[x][1] != nums[x]:
                return find(parent, nums.index(parent[x][1]), cnt)
            return nums[x]

        root = list()
        parent = list()

        for num in nums:
            parent.append([num, num])
            
        for i in range(len(nums)):
            for j in range(0, i):
                if not is_disjoint(nums[i], nums[j]):
                    parent[j][1] = nums[i]

        for i in range(len(nums)):
            root.append(find(parent, i, 0))
            
        return max(Counter(root).values())
