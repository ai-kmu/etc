class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 만약 숫자들이 groupSize로 나눴을 때 0이 아니라는 것은 애초에
        # groupSize만큼 숫자들을 나눌 수 없는 경우이기 때문에 False 반환
        if len(hand) % groupSize != 0:
            return False
        
        # hand를 정렬해서 new_hand로 선언
        # groupSize 크기만큼 숫자를 나눠 담을 배열 선언
        # loop를 돌만큼 숫자 계산
        new_hand = sorted(hand)
        rearrange = []
        loop = len(hand) // groupSize

        # 먼저 loop를 돌며 prev_num을 -1로 초기 설정
        for i in range(loop):
            prev_num = -1
            # new_hand를 돌며 curr_num을 현재 new_hand의 원소로 설정
            for j in range(len(new_hand)):
                curr_num = new_hand[j]
                
                # 만약 rearrange의 크기가 groupSize만큼 들어갔다면 안쪽 loop종료
                if len(rearrange) == groupSize:
                    break
                
                # 만약 prev_num과 curr_num이 같다면 중복된 숫자이므로 continue
                elif prev_num == curr_num:
                    continue
                
                # 현재 숫자를 rearrange에 넣어주고 prev_num업데이트
                rearrange.append(curr_num)
                prev_num = curr_num
            
            # 만약 rearrange의 마지막 숫자에서 처음 숫자를 뺀 후 + 1을 해줬을 때
            # groupSize와 같지 않다면 False 반환 -> rearrange 안의 숫자가 1씩
            # 증가하는지 확인하기 위함
            if rearrange[-1] - rearrange[0] + 1 != groupSize:
                return False
            
            # 만약 rearrange에 숫자가 담겨 있다면 new_hand로부터 remove를 통해 숫자 제거
            elif len(rearrange) > 0:
                for _ in range(len(rearrange)):
                    remove_num = rearrange.pop()
                    new_hand.remove(remove_num)
                    
        # 최종적으로 new_hand에 숫자가 없으면 True 반환
        return True if len(new_hand) == 0 else False
