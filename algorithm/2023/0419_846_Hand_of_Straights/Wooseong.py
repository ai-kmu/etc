from collections import defaultdict as ddict

class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        # 예외처리: 일단 gs의 배수에 해당하는 개수만큼 카드가 있어야 됨
        if len(hand) % gs:
            return False

        # card 종류마다 몇 개 남았는지 세기
        remain = ddict(lambda: 0)
        for card in hand:
            remain[card] += 1

        # 정렬해놓고 greedy 탐색
        hand.sort()
        for card in hand:
            # 해당 card가 남아 있지 않으면 건너뜀
            if not remain[card]:
                continue

            # 문제 조건을 맞추기 위해서는
            # 현재 카드를 기준으로 연속적으로 groupSize(gs) 만큼의 카드가 있어야 됨
            # -> 현재카드(card + 0) 포함해서 gs번째카드(card + gs - 1)까지 있어야 됨
            for i in range(gs):
                # ddict로 해뒀기 때문에 애초에 없었거나 다 쓰면 0을 반환
                # == 문제 조건 불충족
                if not remain[card + i]:
                    return False
                
                # 사용하면 하나 빼기
                remain[card + i] -= 1

        return True
