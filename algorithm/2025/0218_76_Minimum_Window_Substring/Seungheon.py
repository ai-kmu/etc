from collections import Counter
from collections import deque

class Solution(object):
    def minWindow(self, s, t):

        # close_dict에 있는 가장 왼쪽에 있는 idx찾는 함수. (close_dict는 아래 설명있음)
        def left_index(close_dict):
            left_idx = float('inf')
            for k in close_dict.keys():
                if close_dict[k][0] is None:
                    return None
                else:
                    left_idx = min(close_dict[k][0], left_idx)

            return left_idx
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_dict = Counter(list(t))

        # key의 가장 인접한 N개의 idx를 저장하는 dictionary / N은 t에 존재하는 key의 수 / FIFO를위해 deque사용
        close_dict = {}
        for k in t_dict.keys():
            c_num = t_dict[k]
            close_dict[k] = deque([None for _ in range(c_num)])

        answer = ""
        for idx, c in enumerate(s):

            # t안에 있으면
            if c in t_dict.keys():
                close_dict[c].popleft()
                close_dict[c].append(idx)
                
                # 가장 왼쪽 idx찾기, 아직 key가 모두 없으면 None을 출력
                left_idx = left_index(close_dict)
                if left_idx is not None:
                    if answer == "" or idx + 1 - left_idx < len(answer):
                        # print(idx,left_idx)
                        answer = s[left_idx:idx + 1]

            # 없으면 아무것도 안함
            else:
                continue

        return answer
