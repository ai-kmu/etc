class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        # reward1과 reward2의 차이를 구하고, 인덱스를 포함한 리스트로 변환
        indexed_diff = []
        for index in range(len(reward1)):
            diff = reward1[index] - reward2[index]
            indexed_diff.append((diff, index))
        
        # 차이값을 기준으로 내림차순 정렬
        # 차이값이 큰 순서대로 정렬하면서 최적의 값을 얻을 수 있게됨
        # 차이값이 양으로 클 경우 reward2의 값이 상대적으로 작을 가능성이 높음.(상대적 이득을 계산)
        indexed_diff.sort(reverse=True, key=lambda x: x[0])
        
        total_reward = 0
        # reward1에서 고른 index값을 안고르기 위해
        # list를 쓰면 시간복잡도 때매 set을 사용
        selected = set()

        # 가장 큰 차이를 가진 k개의 인덱스에 대해 reward1의 값을 더함
        for j in range(k):
            index = indexed_diff[j][1]
            total_reward += reward1[index]
            selected.add(index)
        
        # 나머지 인덱스에 대해서는 reward2의 값을 더함
        for i in range(len(reward2)):
            if i not in selected:
                total_reward += reward2[i]

        return total_reward