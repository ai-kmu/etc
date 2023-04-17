class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # trivial case
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        # hand를 정렬한 후 순회
        hand.sort()
        table = {}
        
        for card in hand:
            # 만약 들어갈 수 있는 group이 있다면
            if card in table:
                # groupd 중 아무거나 pop한 후 count에 1을 뺴고 다시 table에 추가한다
                count = table[card].pop()
                if not table[card]:
                    del table[card]
                if count > 1:
                    table[card+1] = table.get(card+1, []) + [count-1]
            # 없을 경우 새로운 group을 만든다
            else:
                table[card+1] = table.get(card+1, []) + [groupSize-1]
        
        return not table
