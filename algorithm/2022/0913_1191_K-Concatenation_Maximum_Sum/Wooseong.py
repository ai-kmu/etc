class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 계속 사용할 상수 선언
        modulo = 1e9 + 7
        n = len(arr)
        
        # DP 한 번 update 하는 함수: 두 번 써야 해서 코드 줄이기 위해 함수화
        def update_DP(max_, cycle):
            for i, elem in enumerate(arr):
                # DP[0]을 맨 처음 갱신할 때는 양수인 elem이나 0을 그대로 갖고 오면 됨
                if i == 0 and cycle == 0:
                    DP[i] = max(elem, 0)
                    
                # 다른 때는 이전 + elem
                # 결과가 음수면 0
                # 파이썬은 -1이 오른쪽 끝을 index하기 때문에 i=0일 때도 사용 가능
                else:
                    DP[i] = DP[i - 1] + elem
                    if DP[i] <= 0:
                        DP[i] = 0
                # max값 업데이트 - max(DP)보다 효율적
                max_ = max(max_, DP[i])
                    
            return max_
        
        
        # DP, max값 초기화
        DP = [-1] * n
        max_ = 0
        
        # k=1이면 업데이트 한 번만 해서 끝
        if k == 1:
            answer = update_DP(max_, 0)
        
        # 아닐 때는 k번 반복한 arr를 다 가져올 수 있을 때, 없을 때로 나눔
        else:
            # 두 번만 반복해서 이전 / 이후 비교
            for cycle in range(2):
                max_ = update_DP(max_, cycle)
                if cycle == 0:
                    prev = DP[-1]
                    max_prev = max_
            
            # 없을 때 == DP를 업데이트 해도 동일한 상태가 됨
            if DP[-1] == prev:
                answer = max_
            # 있을 때 -> k번 반복할 필요 없음
            # DP_new = DP_prev + sum(arr)이기 때문임 
            else:
                answer = max_ + (k - 2) * (max_ - max_prev)
                
        return int(answer % modulo)
