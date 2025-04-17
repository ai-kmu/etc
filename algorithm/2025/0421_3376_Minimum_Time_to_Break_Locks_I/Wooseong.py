class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        # sort 안해도 상관 없지만,
        # 그래도 이왕이면 센 거부터 푸는 게 좋을듯
        strength = tuple(sorted(strength, reverse=True))

        # @lru_cache : 이거 넣으면 캐싱으로 속도를 빠르게 어쩌구..
        @lru_cache
        def dp(remain, x):
            # 탈출 조건
            if len(remain) == 0:
                return 0
            
            # 일단 무한대로 init
            result = float('inf')
            # lock들 하나씩 보면서
            for i, lock in enumerate(remain):
                # 이 lock을 풀기 위해 기다려야 하는 시간
                time = (lock + x - 1) // x
                # 풀었으니까 버리고
                new_remain = remain[:i] + remain[i + 1:]

                # `time` : 이걸 풀면 걸리는 시간
                # `dp()` : 남은 거(`new_remain`)에 대한 최솟값
                # `curr` : 그 둘을 더한 게 이번 `lock`을 풀었다 쳤을 때의 시간
                curr = time + dp(new_remain, x + k)

                # 그거랑 현재 함수 내에서의 `result` 중에서 최솟값으로 업데이트 하고
                result = min(result, curr)

            # `remain` 다 돌고 나서의 최솟값 반환            
            return result
        
        # 그게 답이 됨
        return dp(strength, 1)
