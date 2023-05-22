class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        sp = 0  # window?의 시작점 (start point)
        cp = 0  # 끝점이자 현재 탐색하는 위치 (current point)

        # sliding window..?
        for cp in range(len(nums)):
            # 현재 포인트가 0이면 뒤집어봄
            if nums[cp] == 0:
                k -= 1
            
            # 근데 그게 안 된다면
            if k < 0:
                # 시작점 (왼쪽 끝)이 0이라면
                # -> 뒤집었던 거니까 다시 돌리고 당기기
                if nums[sp] == 0:
                    k += 1
                # 아니라면 당기기만
                sp += 1
        
        # 끝나면 답은 이렇게 계산 됨
        return cp - sp + 1

# 무지성으로 그냥하긴 했는데,
# 이게 왜 되는지 모르겠음.
# 뭔가 max를 어디선가는 계산해야될 거 같은데...
