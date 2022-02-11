class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits array: fruit type, 가능한한 많은 fruit 수집
        # 2개의 baskets, 한 basket에 single type만 가능, 오른쪽으로만 가능
        # maximum fruit 구하기
        
        answer = 0
        curr_fruit = 0
        first = [fruits[0], 0]
        second = [None, 0]
        
        for i, typ in enumerate(fruits):
            # 현재이면 업데이트, 아니라면 두번째 할당 및 업데이트
            if first[0] == typ: #first update
                first[1] += 1
                if i > 0 and fruits[i-1] != typ: # 연속적이지 않을 때
                    first[1] = 1
            elif second[0] is None: # second가 None일때 새로 할당
                second = [typ, 1]
            elif second[0] == typ: # second update
                second[1] += 1
                if i > 0 and fruits[i-1] != typ: # 연속적이지 않을 때
                    second[1] = 1
            else: # 3번째 type이 나왔을 때 update
                first = second if second[0] == fruits[i-1] else first
                curr_fruit = first[1]
                second = [typ, 1]
            curr_fruit += 1
            answer = max(curr_fruit, answer)
            
        return answer
