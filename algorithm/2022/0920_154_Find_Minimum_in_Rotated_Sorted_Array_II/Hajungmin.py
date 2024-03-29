# heap 사용
from heapq import heappop, heapify

class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapify(nums)
        return heappop(nums)
    
# min 사용
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    
# 이분 탐색
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 처음 지점과 마지막 지점 설정
        start = 0
        end = len(nums) - 1
        
        # 멈출 조건문을 걸어주고 루프를 돈다
        while start < end:
            # 중간 값 설정
            mid = (start + end) // 2
            
            # 만약 중간 값이 끝 값보다 크다면 시작점은 중간 값에 1을 더해서 옮겨준다.
            if nums[mid] > nums[end]:
                start = mid + 1
            
            # 만약 중간 값이 끝 값보다 작으면 끝 값을 중간으로 옮겨준다.
            elif nums[mid] < nums[end]:
                end = mid
            
            # 만약 중간 값이랑 끝값이랑 같으면 탐색 범위를 1씩 줄이면서 탐색한다
            else:
                end -= 1
        
        return nums[start]

# for ~ else 문을 통해 중간에 return => 일반적으로 가장 빠르게 나옴
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 처음 값으로 ans 선언
        ans = nums[0]
        
        # nums를 돌며 값이 감소하는 곳이 나오면 그 곳이 rotation하기 전 시작점이기 때문에 return
        # for문이 문제없이 돌게되면 값이 계속 상승한 것이기 때문에 rotation이 이뤄지지 않은 것이므로 ans return
        for i in nums:
            if ans > i: return i
        
        else:
            return ans
