# 왼쪽, 오른쪽 중 큰 쪽이 더 커지는 것은 의미가 없음
# 왼쪽, 오른쪽 중 작은 쪽이 커지는 것이 합리적

class Solution:
    def maxArea(self, height):
        length = len(height)
        P = [0, 1] # 왼쪽 오른쪽 저장, 오른쪽은 -1로부터 움직일것
        
        get_weight = lambda a,b : ((length-b-a) * min(height[a], height[-b])) # 현재 위치의 넓이를 구하는 함수

        max_weight = -1 # max weight 초기화
        while(P[0] + P[1] < length):
            max_weight = max(get_weight(P[0], P[1]), max_weight)
            P[height[P[0]] > height[-P[1]]]+=1 # 뭐가 크냐에 따라 어디에 1을 더해줄지 결정
            
        return max_weight
