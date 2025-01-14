class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flag = 0
        temp = []
        while True:
            if len(nums) == 1:
                break
            for i in range(0, len(nums)-1,2):
                if flag == 0:
                    temp.append(min(nums[i], nums[i+1]))
                    flag += 1
                else:
                    temp.append(max(nums[i], nums[i+1]))
                    flag = 0
                    
            nums = temp
            temp =[]
#             print(nums)
#             num = temp
#             for j in range(len(num)-1,2):
                
                

#         print(nums)

        return nums[-1]
