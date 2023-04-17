class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # heapq를 사용하여 풀이 

        # hand 길이가 groupSize로 나눠지지 않는다면 바로 False
        if len(hand) % groupSize != 0:
            return False
        
        # hand 길이와 groupSize가 같다면 숫자가 이어지는지 확인 
        if len(hand) == groupSize:
            hand.sort()
            for i in range(len(hand)-1):
                if hand[i] + 1 != hand[i+1]:
                    return False

        # 힙으로 만듬 
        heapq.heapify(hand)
        # temp는 연속적이지 않은 숫자들이 들어갈 임시 저장소 
        temp = []
        # group은 groupSize만큼의 연속된 숫자들이 들어갈 저장소
        first = heapq.heappop(hand)
        group = [first]

        while hand:
            # 현재 수를 heappop해주면 가장 작은수가 반환됨 
            now = heapq.heappop(hand)

            # group이 groupSize만큼 찼다면 새로 초기화 
            if len(group) == groupSize:
                group = [now]
                continue

            # group의 마지막 값과 현재 값이 1 차이라면 group에 now값 추가 
            if group[-1] + 1 == now:
                group.append(now)
                # 연속된 값을 추가해줬으므로 
                #그동안 연속적이지 못했거나 now와 동일했던 값들을 
                # 따로 temp에 모아 뒀다가 다시 hand에 넣어줌 
                if temp:
                    for j in range(len(temp)):
                        heapq.heappush(hand, temp[j])
                    temp = []
            # 연속적이지 않은 값이라면 temp에 임시 저장 
            else:
                temp.append(now)

        # hand는 다 pop했지만 temp가 남아있는 경우 
        # temp에 연속적인 수가 들어있는지 확인
        if temp:
            if group[-1] + 1 != temp[0]:
                return False 

        
        # 모든 경우를 통과했다면 True 반환
        return True
