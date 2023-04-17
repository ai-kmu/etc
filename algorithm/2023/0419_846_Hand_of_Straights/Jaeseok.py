from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        # 어떻게 해도 arrange가 불가능한 경우
        if n % groupSize != 0:
            return False
        # 전체 숫자의 갯수를 count한 dictionary
        num_count = Counter(hand)
        # 전체 숫자만큼 다 세면 True 반환
        while n != 0:
            # num_count의 key에서 최솟값을 뽑음
            num = min(num_count.keys())
            # groupSize의 크기만큼 순회하면서
            for i in range(groupSize):
                # 아직 다 못 돌았는데 더 셀 숫자가 없으면 무조건 False
                if num_count[num+i] == 0:
                    return False
                # num_count에서 숫자를 빼는데
                num_count[num+i] -= 1
                # 0이 되면 num_count에서 key를 없앰
                if num_count[num+i] == 0:
                    del(num_count[num+i])
                n -= 1
        return True
