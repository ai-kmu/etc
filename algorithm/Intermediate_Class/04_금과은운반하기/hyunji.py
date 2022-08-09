# 오답
# 시간을 기준으로 parametric search 사용
import math

def solution(a, b, g, s, w, t):
    start = 0
    # 대략 최대 시간 계산: 10^5(t[i]) * 10^9(g[i],s[i]) * 10
    end = 10 ** 15
    mid = 0
    
    while start <= end:
        gold = 0
        silver = 0
        total = 0
        mid = (start + end) // 2
        
        for i in range(len(g)):
            # mid 시간 동안 트럭의 이동 가능 횟수 (편도)
            if mid//t[i] > 0:
                move = mid//t[i]
            
            # mid 시간 동안 옮길 수 있는 총 광물의 양
            total = math.ceil(move/2) * w[i]
            
            # 총 광물 양 안에서 gold랑 silver 운반 비율을 어떻게 정할지 모르겠어요..
            gold += g[i] 
            silver += s[i]
        
        # 목표치보다 광물 양이 금, 은 둘다 더 많으면
        if gold >= a and silver >= b:
            # end 1만큼 감소
            end -= 1 
        else:
            start += 1
            
    return mid
