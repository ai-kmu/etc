# 답보고 풀었습니다.
# 풀이는 안해주셔도 되요

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = Counter(hand)
        cards = sorted(freq.keys())
        for card in cards:
            while freq[card] > 0:
                for i in range(groupSize):
                    if freq[card+i] <= 0:
                        return False
                    freq[card+i] -= 1
        return True
