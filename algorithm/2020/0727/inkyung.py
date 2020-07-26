class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = list()
        max_len = 0
        for char in s:
            if char not in answer:                      # 없는 char인 경우 추가
                answer.append(char)
            else:
                max_len = max(len(answer), max_len)     # max_len 갱신
                answer.append(char)
                start_idx = answer.index(char) + 1      # 이미 있는 단어이므로 idx를 만들어서
                answer = answer[start_idx:]             # answer 리스트를 새롭게 갱신
        
        max_len = max(len(answer), max_len)
        return max_len

