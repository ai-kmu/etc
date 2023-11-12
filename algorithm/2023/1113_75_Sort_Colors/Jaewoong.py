class Solution(object):
    def sortColors(self, nums):
        # 0,1,2 세는 카운터
        count0s = 0
        count1s = 0
        count2s = 0
        # nums에 따라 0,1,2 개수를 셈
        for idx in range(len(nums)):
            if nums[idx] == 0:
                count0s += 1
            elif nums[idx] == 1:
                count1s += 1
            elif nums[idx] == 2:
                count2s += 1
        
        idx = 0;
        # counts가 빠질때까지 숫자 순서대로 채움
        while (count0s > 0):
            nums[idx] = 0
            idx += 1
            count0s -= 1
        
        while (count1s > 0):
            nums[idx] = 1
            idx += 1
            count1s -= 1
        
        while (count2s > 0):
            nums[idx] = 2
            idx += 1
            count2s -= 1
