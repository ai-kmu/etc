class Solution:
    def jump(self, nums: List[int]) -> int:
        can_jump = []
        for idx, val in enumerate(nums):           # 각 자리에서 최대로 뛸 수 있는 index를 저장
            can_jump.append(idx + val)
        
        last = len(nums) - 1                       # 마지막 index
        num = 0                                    # 뛴 횟수
        while last > 0:                            # index 0에 도착할 때까지
            for idx, val in enumerate(can_jump):   
                if val >= last and idx < last:     # 마지막 jump한 곳까지 도착할 수 있고 index가 가장 작은 자리를 이전 자리로 선 
                    last = idx
            num += 1
        return num
