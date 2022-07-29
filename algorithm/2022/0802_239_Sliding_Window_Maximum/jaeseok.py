from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []
        # monotonic increasing queue 구현
        for i in range(len(nums)):
            # 큐에서 가장 왼쪽이 더 이상 영향을 미칠 수 없게 됐을 때 pop
            while q and q[0][1] <= i - k:
                q.popleft()
            # 큐에서 가장 오른쪽이 앞으로 들어올 숫자보다 클 때까지 pop
            while q and q[-1][0] <= nums[i]:
                q.pop()
            # 큐에는 앞으로 들어올 숫자와 그 위치가 저장됨
            q.append((nums[i], i))
            # 가장 왼쪽의 숫자가 영향을 미치는 범위 내에서의 가장 큰 숫자이므로 answer에 추가
            answer.append(q[0][0])
            # 슬라이딩 윈도우가 형성되는 때부터가 정답
        return answer[k - 1:]
