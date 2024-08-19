class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # k: 첫 번째 쥐가 먹을 수 있는 치즈 양

        # 쥐 1이 아예 먹을 수 없는 경우
        if k == 0:
            return sum(reward2)
        
        # 쥐 1이 전부 먹는 경우
        elif k == len(reward1):
            return sum(reward1)
        
        else:
            reward_pair = []
            answer = 0

            # heappop 활용을 위해 최대 힙으로 구현
            for i in range(len(reward1)):
                heapq.heappush(reward_pair, [-(reward1[i] - reward2[i]), reward1[i], reward2[i]])

            # reward1[i] - reward2[i]의 차가 큰 경우: 쥐 1이 먹는 게 더 이득
            # 쥐 1이 총 k번 치즈를 먹음
            for _ in range(k):
                cheese = heapq.heappop(reward_pair)
                answer += cheese[1]

            # 나머지는 전부 쥐 2가 먹음
            answer += sum(cheese[2] for cheese in reward_pair)
        
        return answer
        
