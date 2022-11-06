class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        
        nums.sort()
        
        answer = set() # 밑에서 중복방지를 위한
        
        for i in range(n):
            
            for j in range(i + 1, n): # 4개의 pointer 사용
                
                x = j + 1
                y = n - 1
                
                while x < y:
                    
                    sum_val = nums[i] + nums[j] + nums[x] + nums[y]
                    
                    if sum_val > target: y -= 1
                        
                    elif sum_val < target: x += 1
                        
                    else:
                        ans = (nums[i], nums[j], nums[x], nums[y])
                        answer.add(ans)
                        x += 1
                        y -= 1 # 포인터 이동
        return answer
