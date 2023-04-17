'''
시간초과 코드 -> 딕셔너리를 순회할때 시간초과가 발생하는듯 함
'''


from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand, groupSize):
        # 총 길이가 size에 나누어 떨어지지 않으면 무조건 False
        if len(hand) % groupSize != 0:
            return False
        
        freq = defaultdict(int)
        
        # 리스트의 원소마다의 개수를 계산
        for num in hand:
            freq[num] += 1
        
        sorted_hand = sorted(hand)

        for i in range(len(sorted_hand)):
            if freq[sorted_hand[i]] > 0:
                for j in range(groupSize):
                    # 딕셔너리에 없거나 이미 다 사용한 숫자가 필요한 경우
                    if sorted_hand[i] + j not in freq or freq[sorted_hand[i] + j] <= 0:
                        return False
                    # 딕셔너리에서 값을 하나 제거
                    freq[sorted_hand[i] + j] -= 1
        
        return True
