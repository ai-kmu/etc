class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        
        if len(hand) == groupSize:
            hand.sort()
            for i in range(len(hand)-1):
                if hand[i] + 1 != hand[i+1]:
                    return False

        heapq.heapify(hand)

        first = heapq.heappop(hand)
        temp = []
        group = [first]


        while hand:
            now = heapq.heappop(hand)

            if len(group) == groupSize:
                group = [now]
                continue


            if group[-1] + 1 == now:
                group.append(now)
                if temp:
                    for j in range(len(temp)):
                        heapq.heappush(hand, temp[j])
                    temp = []
            else:
                temp.append(now)

        if temp:
            if group[-1] + 1 != temp[0]:
                return False 

        

        return True
