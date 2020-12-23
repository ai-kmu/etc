class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        front = -1
        back = -1
        sort_nums = sorted(nums)         # 정렬
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:  # 정렬된 리스트랑 다른 곳을 찾음
                if front == -1:          # 앞인지 뒤인지 찾음
                    front = i
                else:
                    back = i
        if front == -1:                  # 틀린 곳이 없다면 0 반환
            return 0
        return back - front + 1          # 바꿔야하는 숫자의 개수를 반환
    
    
    
    # [1, 4, 2, 8, 10]
    # 1인 경우 -> [], 1, [4, 2, 8, 10]
    # 2인 경우 -> [1], 4, [2, 8, 10]
    # 3인 경우 -> [1, 4], 2, [8, 10]
    # 4인 경우 -> [1, 4, 2], 8, [10]
    # 5인 경우 -> [1, 4, 2, 8], 10, []
