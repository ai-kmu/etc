class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # 이분탐색해서 최솟값을 찾습니다
        while left < right:
            
            # 중앙 위치를 mid에 저장합니다
            mid = (left + right) // 2
            print(nums[mid])
            # nums[mid] > nums[right] 인경우 최솟값이 우측에 있는것을 알 수 있습니다..
            if nums[mid] > nums[right]:
                left = mid + 1
            # 양끝값이 같은 경우에 대한 예외처리
            elif nums[left] != nums[right]:
                # 중앙값이 최솟값일 수도 있기에 중앙값도 확인해줍니다.
                right = mid
            # 양끝값이 같은경우 왼쪽값을 한칸 움직여서 다시 탐색합니다.
            else:
                left += 1
        return nums[left]
