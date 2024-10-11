class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        counter = dict()
    
        for i, val in enumerate(nums):
            counter[val] = i
        
        for i, val in enumerate(nums):
            try: 
                target_i = counter[target-val]
                if i == target_i:
                    continue
                return [min(i, target_i), max(i, target_i)]
            except:
                pass
