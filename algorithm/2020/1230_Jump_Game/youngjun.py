class Solution:
    def canJump(self, nums: List[int]) -> bool:
        answer=False
        d_idx = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1): #마지막 도착 d_idx를 앞으로 이동하기
            if nums[i] + i >= d_idx:
                d_idx = i

        if d_idx==0:
            answer=True
        #마지막에 d_idx가 연결된지 확인
        return answer
