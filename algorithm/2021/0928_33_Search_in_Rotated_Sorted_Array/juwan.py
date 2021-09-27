class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left , right = 0, len(nums) - 1 # 바이너리 탐색 설정
        while left <= right :
            center = left + (right - left) // 2 # 이진 탐색 시작
            if nums[center] == target: # 찾으면
                return center # 정답 리턴
            if center + 1 < len(nums) and target == nums[center + 1]:
                return center  + 1 # 중앙값에서 좌/우에 있는 요소까지 탐색, 조건은 배열을 초과하지 않는 선에서.
            if center -1 >= 0 and target == nums[center - 1]:
                return center - 1

            # 만약 정답을 찾지 못했다면 
            
            if  nums[left] < nums[center]:  # 현재 중앙겂이 왼쪽보다 클 때,
                if target >= nums[left] and target <= nums[center]:
                    right = center - 1 # 타겟이 맨 왼쪽보다 오른쪽에 있고 이전 중앙값보다 왼쪽에 있으면, 오른쪽 범위를 현재의 중앙값 - 1로 옮겨서 반토막을 잘라냄.
                else:
                    left = center + 1
                    
            else: # 현재 중앙값이 왼쪽 끝보다 작아졌을 때,
                if target >= nums[center] and target <= nums[right]:
                    left = center + 1
                else:
                    right = center - 1
        return -1
