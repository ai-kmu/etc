from collections import defaultdict, Counter
from copy import deepcopy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # len s < len t 이면 애초에 불가능
        if len(s) < len(t):
            return ""
        
        # t에 포함된 문자, 해당 인덱스 저장
        sub_s = ""
        min_sub_s = s[::]
        idx_s = []

        for idx, c in enumerate(s):
            if c in t:
                sub_s += c
                idx_s.append(idx)

        # 횟수와 minimum window일 때의 횟수 저장하는 Counter
        cnt_t = Counter(t)
        result_cnt_t = deepcopy(cnt_t)
        end_s = 0

        # 투 포인터로 탐색
        # substring 구할 때 start는 len(sub_s) - len(t)까지만 계산하면 됨
        for start_s in range(len(sub_s) - len(t) + 1):
            # end index늘려가며 substring 탐색 : cnt_t의 값이 모두 0 이하이면 substring
            while not all([i <= 0 for i in cnt_t.values()]) and (end_s < len(sub_s)):
                cnt_t[sub_s[end_s]] -= 1
                end_s += 1

            # substring이고 길이가 더 작으면 min_sub_s에 저장, result_cnt_t 업데이트
            if all([i <= 0 for i in cnt_t.values()]) and (len(min_sub_s) >= (idx_s[end_s - 1] - idx_s[start_s] + 1)):
                min_sub_s = s[idx_s[start_s]:idx_s[end_s - 1] + 1]
                result_cnt_t = deepcopy(cnt_t)

            # 마지막 탐색 시에는 다시 cnt_t 횟수를 증가시킬 필요 없음
            if start_s < len(sub_s) - len(t):
                cnt_t[sub_s[start_s]] += 1

        # substring을 최종 Counter dict가 만족했으면 min_sub_s 반환 아니면 "" 반환
        return min_sub_s if all([i <= 0 for i in result_cnt_t.values()]) else ""
