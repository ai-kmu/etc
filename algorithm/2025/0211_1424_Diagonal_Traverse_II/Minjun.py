from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        a = defaultdict(list)        
        # 인덱스 합이 같으면 같은 대각선
        # 다 담아있.
        for i, k in enumerate(nums):
            for j, v in enumerate(k):
                a[i+j].append(v)
        d =[]
        # 뒤집어서 담아있
        for i in a.values():
            for k in i[::-1]:
                d.append(k)
        return d
