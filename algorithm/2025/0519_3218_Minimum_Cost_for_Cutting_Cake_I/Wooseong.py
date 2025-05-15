class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        """Greedy"""

        # 그리디를 위한 정렬
        h_cost = sorted(horizontalCut, reverse=True)
        v_cost = sorted(verticalCut, reverse=True)

        # 값 초기화
        h_cut, v_cut = 0, 0  # 해당 방향으로 현재 얼마나 잘랐는지
        h_seg, v_seg = 1, 1  # 잘려서 조각이 몇 개 생겼는지
        cost = 0             # 누적 cost

        # 값이 높은 순으로 일단 숭덩숭덩 자름
        while h_cut < (m - 1) and v_cut < (n - 1):
            # h 값이 높으면 h로, v가 높으면 v로 자름
            # 자를 때는 해당 방향 "전체" 잘라서, `x *_seg`가 필요함
            if h_cost[h_cut] >= v_cost[v_cut]:
                cost += h_cost[h_cut] * v_seg
                h_seg += 1
                h_cut += 1
            else:
                cost += v_cost[v_cut] * h_seg
                v_seg += 1
                v_cut += 1

        # 남아 있는 조각 자르기
        # 수직
        while h_cut < (m - 1):
            cost += h_cost[h_cut] * v_seg
            h_cut += 1

        # 수평
        while v_cut < (n - 1):
            cost += v_cost[v_cut] * h_seg
            v_cut += 1

        return cost

    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        """DP"""
        
        # 그냥 하면 TLE 터지길래, sorting을 좀 해봄
        # 그러면 이제 '횟수'가 분할 기준이 됨.
        h_cost = sorted(horizontalCut, reverse=True)
        v_cost = sorted(verticalCut, reverse=True)

        @lru_cache
        # idx : 현재 위치
        # cnt : 몇 개나 잘렸는지
        def dp(h_idx, v_idx, h_cnt, v_cnt):
            # idx 넘어감 == 다 자름 -> 탈출 조건
            if h_idx == (m - 1) and v_idx == (n - 1):
                return 0
            
            min_cost = float("inf")  # 초기화: 큰 값

            # 행 탐색
            if h_idx < (m - 1):
                cost = h_cost[h_idx] * v_cnt                     # 한 방향으로 전체 절단
                remain = dp(h_idx + 1, v_idx, h_cnt + 1, v_cnt)  # 그랬을 때 남은 부분 자르는 비용
                min_cost = min(min_cost, cost + remain)          # dp 갱신

            # 열 탐색
            if v_idx < (n - 1):
                cost = v_cost[v_idx] * h_cnt                     # 한 방향으로 전체 절단
                remain = dp(h_idx, v_idx + 1, h_cnt, v_cnt + 1)  # 그랬을 때 남은 부분 자르는 비용
                min_cost = min(min_cost, cost + remain)          # dp 갱신

            return min_cost
        
        return dp(0, 0, 1, 1)
