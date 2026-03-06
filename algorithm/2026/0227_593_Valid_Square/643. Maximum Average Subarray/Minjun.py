class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[0:k])/k
        tmp = sum(nums[0:k])/k
        # print(ans)
        for i in range(1, len(nums)-k+1):
            # print(tmp*k, "-", nums[i-1], "+", nums[i+k-1])
            tmp = tmp*k - nums[i-1] + nums[i+k-1]
            # print(tmp)
            tmp /= k
            # print(tmp)
            if tmp > ans:
                ans = tmp
            
            # a = nums[i:i+k]
            # b = sum(a)/k
            # if b > ans:
            #     ans = b
        return ans
