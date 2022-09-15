'''
< 이분 탐색 >
* 중복 처리: 다를 때까지 당겨오기
1) l <= m: 이 사이엔 없음
    -> left = mid + 1
    따라서 l  > m: right = mid - 1
* 최솟값 업데이트 해주기
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 이분 탐색을 위한 변수 설정
        left = 0
        right = len(nums) - 1
        min_ = nums[left]
        
        # 이분 탐색
        while left <= right:
            # left에서 중복 처리
            while (left < right) and (nums[left] == nums[left + 1]):
                left += 1
            # right에서 중복 처리
            while (left < right) and (nums[right] == nums[right - 1]):
                right -= 1
            
            # 중간 값 설정
            mid = (left + right) // 2
            
            # l <= m 인 경우: left를 당김
            if nums[left] <= nums[mid]:
                min_ = min(min_, nums[left])
                left = mid + 1
            # l > m 인 경우: right를 당김
            else:
                min_ = min(min_, nums[mid])
                right = mid - 1
        
        return min_
