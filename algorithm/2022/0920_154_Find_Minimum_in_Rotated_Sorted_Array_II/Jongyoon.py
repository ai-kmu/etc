"""
특정 값을 기준으로는 오름차순 정렬이 되어 있으므로 binary search를 사용할 수 있다.
mid, end 인덱스의 값을 비교하며 start, mid, end 값을 조정해 나간다.
mid, end 값을 비교하는 이유는 정렬이 되어 있는 상태에서 오름차순이므로 start를 비교해 나가면 더 복잡하게 구현된다.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:   
        
        start = 0
        end = len(nums) - 1
        
        if nums[start] < nums[end]:      # 리스트가 회전하지 않았으면 첫 번째 원소가 가장 작다.
                return nums[start]
        
        while(start < end):               
            mid = (start + end) // 2     # 이진 탐색을 위한 중간점 계산
  
            if (nums[mid] < nums[end]):  # 중간값이 끝값보다 작으면, 중간 ~ 끝 사이에는 최소값이 없으므로 
                end = mid                # 끝값을 중간값으로 바꾸어준다.
            
            elif nums[mid] > nums[end]:  # 중간값이 끝값보다 크면, 중간 ~ 끝 사이에 최소값이 있으므로
                start = mid + 1          # 시작값을 중간값으로 바꾸어준다.
                
            else:                        # 값이 같으면
                end -= 1                 # 끝값을 당겨와서 중복을 제거한다. 오름차순이므로 최솟값은 왼쪽에 있음 -> -1

        return nums[start]
                
            
