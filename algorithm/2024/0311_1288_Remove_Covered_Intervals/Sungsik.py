class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        removed = [False] * n
        
        # arr2가 arr1을 cover하는지 체크
        covered = lambda arr1, arr2: arr1[0] >= arr2[0] and arr1[1] <= arr2[1]
        
        # 모든 interval을 돌며 cover가 되는 쌍이 있는지 체크
        for i in range(n):
            for j in range(n):
                if i == j or removed[j]:
                    continue
                
                removed[i] ^= covered(intervals[i], intervals[j])
                
                if removed[i]:
                    break
        
        return n - sum(removed)
        
