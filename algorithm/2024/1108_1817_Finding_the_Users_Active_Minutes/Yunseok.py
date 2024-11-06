from collections import defaultdict
from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_dict = defaultdict(set)

        for uid, activation_min in logs:
            user_dict[uid].add(activation_min)

        # 사용자 UAM 값에 따른 카운트를 저장할 리스트
        cnt_list = [0] * (k + 1)
        
        # user_dict의 각 사용자를 순회하며 UAM 값을 카운트
        for uam_set in user_dict.values():
            uam = len(uam_set)  # 해당 사용자의 UAM
            if uam <= k:
                cnt_list[uam] += 1

        # 첫 번째 인덱스를 제외하고 결과 반환
        return cnt_list[1:]
