# 1. heap 이용한 최솟값 조회

from heapq import heapify

class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapify(nums)
        return nums[0]
      
# 2. binary search 이용한 최솟값 조회

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 맨 왼쪽과 오른쪽 포인터를 만들어 줌
        l, r = 0, len(nums) - 1

        # ㅣ이 r보다 작은 동안
        while l < r:
            # mid 설정
            mid = (l + r) // 2
            # nums[mid]가 nums[r]보다 크면, 최솟값이 mid와 r 사이에 있다.
            if nums[mid] > nums[r]:
                # 그러므로 l을 mid로 옮겨주어 탐색 범위를 줄인다.
                l = mid
            # nums[mid]가 nums[l]보다 작으면, 최솟값이 mid와 l 사이에 있다.
            elif nums[mid] < nums[l]:
                # 그러므로 r을 mid로 옮겨주어 탐색 범위를 줄인다.
                r = mid
            # [4, 4, 4, 4, 1, 4, 4]의 경우, l, r, mid 셋 다 4이다.
            # 그렇기 때문에 위에서 나온 것처럼 탐색 범위를 좁힐 수 없으므로, r을 앞으로 옮겨주면서 탐색 범위를 줄이고 탐색이 가능하도록 한다.
            else:
                r = r - 1

        return nums[l]

