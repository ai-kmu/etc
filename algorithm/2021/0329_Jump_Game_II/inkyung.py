class Solution:    
    def jump(self, nums: List[int]) -> int:
        
        OPT = [0] * len(nums)
        
        for i in range(1, len(nums)):
            min_value = len(nums)
            
            for j in range(0, i):
                print('j, nums[j]', j, nums[j])
                # 현재 인덱스와 인덱스의 갈 수 있는 거리를 구함
                if j + nums[j]>=i:
                    val = 1 + OPT[j]
                    print('val, minval', val, min_value)
                    if val<min_value:
                        min_value=val
            OPT[i] = min_value
            print(OPT)
        return OPT[-1]
