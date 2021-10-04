class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # list를 정렬 - O(nlogn)
        nums.sort()
        answer = set()
        
        # list를 한번 순회하면서 3sum을 찾음 - O(n)
        for i in range(len(nums)-2):
            # 현재 위치 뒷부분의 값들과의 합이 0이 되는 것을 찾음 - O(n)
            # 제일 작은 값과 큰 값을 고름
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                
                # 만약 3sum이 0보다 작을 경우 작은 값을 크게하고
                # 0보다 클 경우 큰 값을 작게 한다
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(x) for x in answer]
        
            
