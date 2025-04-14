import itertools

class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        mt = float('inf')  # 최소 시간을 무한대로 초기화
        # 모든 가능한 자물쇠 순열을 확인
        for perm in itertools.permutations(strength):
            tt, x = 0, 1  # 현재 시간(tt)과 에너지 증가 계수(x)를 초기화
            for i in perm:
                # 현재 자물쇠를 부수는 데 걸리는 시간 계산 후 누적
                tt += (i + x - 1) // x
                x += K  # 자물쇠를 부신 후 증가 계수 k만큼 증가
            mt = min(mt, tt)  # 지금까지 중 최소 시간 갱신
        return mt  # 최소 시간 반환
