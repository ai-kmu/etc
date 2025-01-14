class Solution:
    def minMaxGame(self, nums: List[int]) -> int:                
        numss = nums
        while len(numss) > 1:
            is_min = True     
            tmp = []

            for i in range(0, len(numss), 2):
                if is_min:
                    tmp.append(min(numss[i:i+2]))
                else:
                    tmp.append(max(numss[i:i+2]))
                is_min = not is_min            
            numss = tmp  
                      
        return numss[0]                        
        
