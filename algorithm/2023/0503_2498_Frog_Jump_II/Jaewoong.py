class Solution:
    def maxJump(self, stones: List[int]) -> int:
        len_list = []
        chk = 0
        # 길이가 2이면
        if len(stones) == 2:
            return stones[1] - stones[0]
        else:
        # 아니면, 증가하는 돌이니까(strictly increasing order) 최대거리는 어쨌건 한칸 더 뛰어서임
            maxjump = []
            for i in range(len(stones)-2):
                jump = stones[i+2] - stones[i]
                maxjump.append(jump)
                jump = 0
                
        return max(maxjump)
