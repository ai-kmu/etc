class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)                            # s의 길이 저장 
        min = -1                                  # min은 -1로 시작
        max = -1                                  # max는 -1로 시작
        while max == -1:                          # max의 값이 바뀌면 반복문 종료
            start = 0                             # substring의 시작 부분 지정
            last = len_s                          # substring의 마지막 부분 지정
            while last != len(s) + 1:             # last가 s의 마지막 부분을 지나친 경우 반복문 종료
                find = 1                          # 찾은지 못 찾은지 확인
                for match in range((last - start)//2):           # substring 길이의 
                    if s[start + match] != s[last - match - 1]:  # 대칭적 자리의 글자가 같은지 확인
                        find = 0                  # palindromic 조건을 만족하지 못하면 find = 0으로 저장
                        break                     # 반복문 종료
                if find == 1:                     # 만약에 찾았으면
                    min = start                   # min은 start로 반환
                    max = last                    # max는 last로 반환
                    break                         # 반복문 종료
                else:                             # palindromic한 substring이 없는 경우
                    start += 1                    # 시작 부분 1 증가
                    last += 1                     # 마지막 부분 1 증가
            len_s -= 1                            # 길이 1 줄이기
            if len_s == 0:                        # 만약 2개의 palindromic한 substring까지 없다면
                min = 0                           # min은 0으로 값 반환
                max = 1                           # max는 1으로 값 반환
        return s[min:max]
