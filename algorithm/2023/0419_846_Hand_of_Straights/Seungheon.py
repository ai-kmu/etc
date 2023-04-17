from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # 각 숫자가 몇개있는지 dictionary만들기
        ddict = defaultdict(int)
        for h in hand:
            ddict[h] += 1

        # key값을 순서대로 정렬
        keys = sorted(ddict.keys())

        # initialization
        start_key_idx = 0
        next_start_key_idx = 0   
        while 1:

            # start 를 변경했는지 여부
            start_chage = True

            for i in range(groupSize):
                # 범위를 벗어나면 false
                if start_key_idx+i >= len(keys):
                    return False
                # 다음값이 연속되는 값이 아니면 false
                if i > 0 :
                    if keys[start_key_idx+i-1] + 1 != keys[start_key_idx+i]:
                        return False 
                # 다음 연속되는 값이 없으면 false
                if ddict[keys[start_key_idx+i]] == 0:
                    return False

                # 사용한값 제거
                ddict[keys[start_key_idx+i]] -= 1
                
                # 사용해서 0이 안되었으면
                if start_chage and ddict[keys[start_key_idx+i]] > 0:
                    next_start_key_idx = start_key_idx+i
                    start_chage = False

            # 다은 순회를 위한 start_key_idx 설정  
            if start_chage:
                start_key_idx = start_key_idx + groupSize
            else:
                start_key_idx = next_start_key_idx

            # 마지막에 도달하였으면 return True
            if start_key_idx == len(keys):
                return True

        return True
