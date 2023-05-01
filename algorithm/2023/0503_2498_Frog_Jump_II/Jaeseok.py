class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        # 예외처리: 돌이 3개부터는 마지막 돌과 첫 돌만 비교
        if n < 4:
            return stones[-1]-stones[0]
        answer = 0
        # 맨 끝은 무조건 도달해야 하므로 추가
        if n % 2 == 0:
            answer = stones[1]-stones[0]
        else:
            answer = max(stones[1]-stones[0], stones[-1]-stones[-2])
        # 나머지 부분은 돌을 한 칸씩 건너뛰면서 최댓값을 갱신해줌
        # forward
        for i in range(0, n-2, 2):
            answer = max(answer, stones[i+2]-stones[i])
        # backward
        for i in range(1, n-2, 2):
            answer = max(answer, stones[i+2]-stones[i])
        return answer
