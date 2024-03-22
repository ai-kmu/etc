class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        q = deque()
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                q.append(i)
        q.append(n)

        i = 0
        subarrays = 0
        
        while len(q) > k:
            minWindowLen = q[k-1]
            nextWindow = q[k]
            subarrays += nextWindow - minWindowLen
            if i == q[0]:
                q.popleft()
            i += 1
        return subarrays
