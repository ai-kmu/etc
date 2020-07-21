class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):                         # 문자열의 처음부터 시작
            length = 1                                  # 길이 1
            char_list = [s[i]]                          # 첫 문자 list에 저장
            for char in s[i+1:]:                        # 다음 문자들을 탐색
                if not char in char_list:               # list에 없는 경우
                    length += 1                         # 길이 +1
                    char_list.append(char)              # list에 추가
                else:                                   # list에 있는 경우
                    break                               # for문 종료
            if length > max_length:                     # 길이가 현재까지 최대 길이보다 더 길다면
                max_length = length                     # 길이 저장
        return max_length                               # 최대 길이 반환
