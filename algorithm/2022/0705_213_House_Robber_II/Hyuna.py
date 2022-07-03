class Solution(object):
    def rob(self, nums):
       
        maxMoney = 0
        visited = [0 for i in range(len(nums))]
        sortedNums = sorted(nums, reverse=True)
        
        for num in sortedNums:
            i = nums.index(num)
            while (visited[i] == 1):
                i = nums.index(num, i+1)
            
            if(i != len(nums) - 1):
                if (visited[i - 1] == 0 and visited[i + 1] == 0):
                    visited[i] = 1
                    maxMoney += num
            else:
                if (visited[i - 1] == 0):
                    visited[i] = 1
                    maxMoney += num
            
        return maxMoney
