class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = set()
        res = 0
        i = 0
        # nums의 length 만큼
        while i < len(nums):
            j = i
            temp = 0 # s 원소가 중복될 때까지
            while j < len(nums):
                if nums[j] not in s: #없으면 넣음
                    s.add(nums[j])
                    temp += 1
                else: break
                j = nums[j] # 
            if temp > res: # 가장 많은 원소를 찾는 것
                res = temp
            i+=1
        
        return res
