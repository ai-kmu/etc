class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        
        answer = 0
        
        for m in range(1, length-1):            # 가운데 병사를 기준으로 낮은 녀석, 높은 녀석을 구하고, 곱해서 구함
            ll = 0  # 왼쪽 낮은 녀석
            lh = 0  # 왼쪽 높은 녀석
            rl = 0  # 오른쪽 낮은 녀석
            rh = 0  # 오른쪽 높은 녀석
            
            for l in range(m):          # 가운데 병사를 옮겨가며 비교
                if rating[l] < rating[m]:
                    ll += 1
                else:
                    lh += 1
            for r in range(m+1,length):
                if rating[m] < rating[r]:
                    rh += 1
                else:
                    rl += 1
            answer += ll*rh + lh*rl     # 곱해서 트리플렛 수 구하기
        return answer
                        
