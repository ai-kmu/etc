class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        tmp = []
        ans = []
        chk = 0
        all_chk = 0
        
        # while all_chk == len(nums)-1:
        print(nums)
        while True:
            for i in range(len(nums)):
                chk+=1
                tmp.append(nums.pop(0))
                if chk == 2:
                    ans.append(min(tmp))
                    tmp = []
                elif chk == 4:
                    ans.append(max(tmp))
                    chk = 0
                    tmp = []    
            if len(ans) != 0:
                nums = ans
            elif len(ans) == 0 :
                break

        print(tmp)
        print('nums', nums)
        return tmp[0]
            

        
