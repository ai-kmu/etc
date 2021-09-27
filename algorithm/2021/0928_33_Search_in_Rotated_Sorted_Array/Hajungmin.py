class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #시작점과 끝점
        start = 0
        end = len(nums) -1
        
        #리스트 안에 숫자가 존재할 때, 루프를 돌게함
        while start <= end:
            #중간 지점을 설정해줌 
            mid = (start + end) // 2
            #만약 중간 지점의 값이 target과 같다면 중간값을 반환해준다
            if nums[mid] == target:
                return mid
            #만약 시작지점값이 중간지점 값보다 작거나 같다면 시작지점의 값과 target을 비교하고 중간지점 값과 target을 비교한다.
            if nums[start] <= nums[mid]:
                # target이 시작점보다 크거나 같고 중간지점보다 작을 경우 끝점을 중간점-1로 변경해준다.
                if nums[start] <= target and nums[mid] > target:
                    end = mid -1
                # 그 외의 경우 시작지점을 중간점+1로 바꿔준다
                else: start = mid +1
            #만약 시작지점 값이 중간지점 값보다 크다면 중간지점과 target을 비교하고 끝점과 target을 비교한다.
            else:
                # 만약 target이 중간값보다 크고 끝값보다 작거나 같을 경우 시작점을 중간점으로 바꿔준다.
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                # 만약 target이 중간보다 작거나 같고 끝점보다 작으면 끝점을 중간점-1로 바꿔준다.
                else: end = mid - 1
        # 리스트 안에 숫자가 존재하지 않을 때, -1을 반환해준다.
        return -1
