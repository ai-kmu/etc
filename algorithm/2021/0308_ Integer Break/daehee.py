class Solution:
    def integerBreak(self, n: int) -> int:

        if n==2: return 1
        if n==3: return 2
        if n==4: return 4
                                # 1은 곱해봐야 의미없으므로 2~4 곱하도록
        three = int((n-2)/3)    # 3을 많이 곱해야 제일 커짐
        remain = (n-2)%3+2      # 3 갯수 구하고 남은 것 구하기
        
        return 3**three * remain
