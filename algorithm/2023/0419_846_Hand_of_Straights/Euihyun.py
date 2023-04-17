# 어디선가 꼬이면서 못풀었습니다.. 그래서 답을 코드입니다

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 손(hand)의 크기가 그룹 크기(groupSize)의 배수가 아니면 False 반환
        if len(hand) % groupSize != 0:
            return False
        
        # 숫자별 개수를 저장하는 딕셔너리 생성
        counter = {}
        for num in hand:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
                
        # 딕셔너리의 키를 오름차순으로 정렬
        sorted_keys = sorted(counter.keys())
        
        # 숫자를 하나씩 읽으면서 그룹이 연속된 값을 가지는지 검사
        for key in sorted_keys:
            count = counter[key]
            if count > 0:
                for i in range(1, groupSize):
                    next_num = key + i
                    # 다음 숫자가 딕셔너리에 없거나 개수가 현재 숫자보다 작으면 False 반환
                    if next_num not in counter or counter[next_num] < count:
                        return False
                    # 딕셔너리의 값을 갱신하여 숫자 개수를 줄임
                    counter[next_num] -= count
                    
        # 모든 숫자가 그룹이 연속된 값을 가지면 True 반환
        return True
