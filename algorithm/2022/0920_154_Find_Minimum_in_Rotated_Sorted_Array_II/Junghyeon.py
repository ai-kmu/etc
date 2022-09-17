class Solution:
    '''
    특정 인덱스를 넘어갈때를 제외하면 모두 오름차순으로 정렬되어 있다.
    -> 감소하기 시작하면 그 인덱스에서의 값이 최솟값
    '''
    def findMin(self, nums: List[int]) -> int:
        
        start_num = nums[0]
        
        # 0번 인덱스의 수와 비교하면서 더 작은 수를 발견하면 그 값이 정답
        for i in nums[1:]:
            if start_num > i:
                return i
        
        # 0번 인덱스의 수가 최솟값인 경우
        return start_num
