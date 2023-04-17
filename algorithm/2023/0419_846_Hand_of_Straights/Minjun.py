from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        # trivial case
        if n % groupSize != 0:
            return False
          
        # 찾기 편하게 정렬
        hand.sort()
        hashing = defaultdict()
        
        # dictionary로 정리
        hashing = {i:0 for i in hand}
        for i in hand:
            hashing[i] += 1
        
        # 현재 들고 있는 가장 작은 친구부터(오름차순) 탐색
        # groupSize만큼 개수 -1
        # 다음 작은 친구 탐색
        for _ in hand[:-groupSize+1]:
            # 손에 들고있는 가장 작은 친구(이전 탐색에서 다 써버리면 건너 뜀)
            if hashing[_] != 0:
                # 썼으니까 개수 -1
                hashing[_] -= 1
                # 지금 녀석부터 groupSize 죄다 -1
                for j in range(1, groupSize):
                    # 없으면 연속해서 groupSize 채우지 못하므로 실패
                    if _+j not in hashing.keys() or hashing[_+j] == 0:
                        return False
                    # 있으면 쓰고 개수 차감
                    hashing[_+j] -= 1
        return 1
