class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        # 2의 제곱을 재정렬하여 power_lsit에 저장
        power_lsit = []
        for i in range(30):
            power_lsit.append(sorted(str(2**i)))

        # n 을 재정렬하여 power_lsit에 있는지 확인
        n = sorted(str(n))
        if n in power_lsit:
            return True
        else:
            return False
