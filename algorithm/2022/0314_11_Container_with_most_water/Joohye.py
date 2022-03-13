# L(left) R(left)의 크기비교를 통해 most water를 contains 하도록한다.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 값 초기화
        L = 0  # L = left
        R = len(height) - 1  # R = right
        answer = 0  # answer = 최종결과값
        width = len(height) - 1  # width = L과R의 너비
        
        # w 제일 작을때 부터 클 때까지
        for w in range(width, 0, -1):
            if height[L] < height[R]:  #L line이 R line 보다 작다면
                L, answer = L + 1, max(height[L] * w, answer)  # L에 +1 해주고 width에 저장, answer에 저장된값과 현재 L에서 구한 넓이값(w와 곱한값) 중 max 한 값을 answer에 저장     
            else:  #L line이 R line 보다 크거나 같다면
                R, answer = R - 1, max(height[R] * w, answer)  # R에 +1 해주고 width에 저장, answer에 저장된값과 현재 L에서 구한 넓이값(w와 곱한값) 중 max 한 값을 answer에 저   
        return answer    
        
