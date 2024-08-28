class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 정령하고 똑같은 list 생성
        n = len(nums)
        nums.sort()
        ans = [i for i in nums]
        
        # 돌면서 i랑 i+1이 같으면 제거
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                del_num = nums[i]
                ans.remove(del_num)
                ans.remove(del_num)

                
        return ans
            
            
