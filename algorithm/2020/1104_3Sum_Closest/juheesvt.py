import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        
        nums.sort()
        print(nums)
        
        length = len(nums)
        differ = sys.maxsize
        
        for i in range(length):
            low = i+1
            high = length-1
            
            while low < high:
                
                # 차이의 절댓값이 최소이면, 차이 및 답 갱신하기
                if abs(nums[i] + nums[low] + nums[high] - target) < differ:                                  
                    differ = abs(nums[i] + nums[low] + nums[high] - target)
                    print(differ)
                    answer = nums[i] + nums[low] + nums[high]
                
                # 차이가 음수면 low를 증가, 아니면 high를 감소
                if nums[i] + nums[low] + nums[high] - target < 0:
                    low +=1
                else:
                    high-=1           
        
        return answer
