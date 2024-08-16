class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        '''
        문제 해석
            - mouse1이 reward1[i]를 먹으면 mouse2는 reward2[i]를 못 먹음
            - mouse1이 k개만 먹었을 때, mouse1이 먹은 reward + mouse2이 먹은 reward를 최대화해야 함
            - mouse1이 i를 먹었을 때 얻을 수 있는 상대적인 reward(reward1[i] - reward2[i])를 구하여 높은 값부터 먹음
        '''
        ans = 0
        relative_reward = list()
        for i in range(len(reward1)):
            relative_reward.append([reward1[i] - reward2[i], i])
        relative_reward.sort(key = lambda x : -x[0])
        cnt = 0
        for i in range(len(reward1)):
            if cnt < k:
                cnt += 1
                ans += reward1[relative_reward[i][1]]
            else:
                ans += reward2[relative_reward[i][1]]
        return ans
