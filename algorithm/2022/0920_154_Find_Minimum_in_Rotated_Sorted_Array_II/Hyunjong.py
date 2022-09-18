class Solution(object):
    # 카운팅 정렬 사용
    def findMin(self, nums):

        count = [0]*10001
        
        for i in range(len(nums)):
            nums[i] += 5000
        
        for i in nums:
            count[i] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        result = [0] * (len(nums))

        for num in nums:
            idx = count[num]
            result[idx - 1] = num
            count[num] -= 1
        
        return result[0] - 5000
