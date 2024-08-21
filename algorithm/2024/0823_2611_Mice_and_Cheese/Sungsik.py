class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # 차이를 구함
        diff = [(x - y, i) for i, (x, y) in enumerate(zip(reward1, reward2))]
        # 가장 큰 k개의 index를 구함
        diff.sort(key=lambda x: -x[0])
        idxes = set([x[1] for x in diff[:k]])
        # k개에 속하면 1번이, 아니면 2번이 먹음
        return sum([x if i in idxes else y for i, (x, y) in enumerate(zip(reward1, reward2))])
