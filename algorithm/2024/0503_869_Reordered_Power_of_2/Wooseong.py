from collections import defaultdict as ddict
# 전략: 10^9보다 작은 2의 거듭제곱은 몇 개 안 됨
# 따라서 이를 모두 set으로 지정하고, 있는지 없는지를 보려고함

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 2의 거듭제곱을 갖는 set 설정
        powers = set()
        power = 1
        # 상한 넘길 때까지 진행
        while power <= 1000000000:
            # n을 reorder할 수 있기 때문에, sort한 상태로 set에 추가
            power_str = ''.join(sorted(str(power)))
            powers.add(power_str)
            power *= 2

        # 주어진 n을 sort
        n = ''.join(sorted(str(n)))
        
        # sort한 게 있는지 여부로 답 반환
        return n in powers
        
