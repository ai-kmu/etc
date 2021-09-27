# binary search를 2번 한다는 느낌으로 풀자
# 우선 binary search로 pivot값을 찾은 후
# pivot을 기준으로 올바르게 다시 정렬한 후
# 이진 탐색을 수행하자

class Solution:
    def search(self, nums, target):
        length = len(nums)
        left = 0
        right = length-1
        
        while(True):
            pivot = (left + right) // 2
            
            if nums[pivot] > nums[right]: # 우리가 찾는 값은 pivot과 right 사이에 존재
                left = pivot + 1
            else: # 우리가 찾는 것은 pivot 왼쪽에 존재
                right = pivot
            if left >= right:
                sorted_list = nums[left:] + nums[:left]
                break
                
        idx = left
        left = 0
        right = length-1
        while(True):
            pivot = (left + right) // 2
            
            if sorted_list[pivot] == target:
                return (pivot + idx) % length
            elif left >= right:
                return -1
            elif sorted_list[pivot] < target:
                left = pivot + 1
            else:
                right = pivot
            
