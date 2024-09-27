# 첫 번째 너무 느려서 다른 거 해봄
# 두 번째 방법이 더 빠른 거 같긴한데 LeetCode 너무 랜덤이라 잘 모르겠음

from collections import deque

class Solution:
    # 세 번 평균 37.7ms (39, 42, 32)
    def reverseWords(self, s: str) -> str:
        # s.split() -> words를 word로 찢음
        # [::-1] -> 순서 뒤집음
        # ' '.join() -> word를 words로 합침
        return ' '.join(s.split()[::-1])

    # 세 번 평균 35.7ms (33, 40, 34)
    def reverseWords(self, s: str) -> str:
        # deque로 word 하나씩 stack 쌓기
        words = deque([])
        word = ''
        for char in s:
            # char가 공백이면
            if char == ' ':
                # word가 있을 경우 (공백이 여러 개 연속되는 경우를 skip하기 위함)
                if word != '':
                    # word를 stack하고 초기화
                    words.appendleft(word)
                    word = ''
                continue
            # char가 공백이 아니면 word 계속 늘리기
            word += char

        # for문 끝났는데 word가 남아 있으면 걔도 stack 하기
        if word != '':
            words.appendleft(word)
        
        # join해서 정답 words 생성
        return ' '.join(words)
            
