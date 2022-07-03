class Solution:
    def rob(self, nums: List[int]) -> int:
        # 만약 숫자가 1개면 그대로 반환
        if len(nums) == 1:
            return nums[0]
        
        # 두 가지 경우의 리스트 선언
        # 하나는 처음을 건너뛰는 경우
        # 다른 하나는 맨 뒤를 제외하는 경우
        res1 = [0,0]
        res2 = [0,0]
        
        # 루프를 돌며 res1[0]에 현재 숫자를 더한 것과 res1[1]의 값 비교
        # res1[0]은 매 루프마다 res1[1]의 값으로 갱신
        # res2도 동일
        for num in nums[1:]:
            res1[0], res1[1] = res1[1], max(res1[0] + num, res1[1])
        
        for num in nums[:-1]:
            res2[0], res2[1] = res2[1], max(res2[0] + num, res2[1])
            
        # 두 경우 중 더 값이 큰 경우 반환
        return max(res1[1], res2[1])
