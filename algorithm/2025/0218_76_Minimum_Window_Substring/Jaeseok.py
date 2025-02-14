# 시간이 너무 오래 걸려서 더 짧게 할 수 있는 방법 생각해봐야 할 듯

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 가장 짧은 답을 갱신해야 하므로 최대 길이 설정
        answer = "A" * 10**5
        # 윈도우의 좌측 포인터, 우측 포인터를 옮겨가면서 조건 확인
        start_idx = 0
        end_idx = 0
        # 카운터를 사용하여 현재 윈도우에 있는 문자 카운트(candidate_count)
        # 포함해야 하는 문자 카운트(correct_count)
        candidate_count = Counter()
        correct_count = Counter(t)
        while True:
            # candidate_count와 correct_count의 교집합이 correct_count -> substring
            if (candidate_count & correct_count) == correct_count:
                cur_answer = s[start_idx:end_idx]
                # 더 짧은 substring일 경우에 answer 갱신
                if len(cur_answer) < len(answer):
                    answer = cur_answer
                # 이제 왼쪽 포인터를 움직이면서 해당 string은 카운터에서 빼주고 더 짧아도 substring인지 체크
                if s[start_idx] in t:
                    candidate_count[s[start_idx]] -= 1
                start_idx += 1
            # substring이 아닐 경우
            else:
                # 이미 우측 포인터가 제일 오른쪽일 경우 더 갱신할 필요 없음
                if end_idx == len(s):
                    return "" if answer == "A" * 10**5 else answer
                # 우측 포인터를 움직이면서 해당 string을 candidate_count에 추가
                if s[end_idx] in t:
                    candidate_count[s[end_idx]] += 1
                end_idx += 1
