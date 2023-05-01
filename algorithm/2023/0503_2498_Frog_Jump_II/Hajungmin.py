class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # 홀수 번째 돌과 짝수 번째 돌들을 따로 선언
        forward = stones[::2]
        backward = [stones[0]] + stones[1::2] + [stones[-1]]
        
        # forward process와 backward process에서 가장 큰 수 초기화
        forward_max = 0
        backward_max = 0
       
        # forward와 backward를 각각 돌며 돌들 사이의 차이를 구함
        # 돌 사이의 차이값 중 가장 큰 수를 계속 업데이트
        for i in range(1, len(forward)):
            dist = forward[i] - forward[i-1]
            forward_max = max(forward_max, dist)
            
        for i in range(1, len(backward)):
            dist = backward[i] - backward[i-1]
            backward_max = max(backward_max, dist)
        
        # forward와 backward 중 큰 값을 반환
        return max(forward_max, backward_max)
