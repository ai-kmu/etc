from collections import deque

class Solution:
    def myAtoi(self, str: str) -> int:
        # 공백 잘라내기
        str = str.lstrip()
        if len(str) == 0:
            return 0
        
        # integer 범위 지정하기
        int_max = 2 ** 31 - 1
        int_min = -(2 ** 31)
        answer = ''
        sign = 1
        

        str = deque(str)

        # 첫 글자가 '+'또는 '-'이면
        # 'sign' 변수를 해당 값으로 설정하고 해당 요소를 제거
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                sign = -1
            str.popleft()

        # str이 빈 문자열이거나 첫 글자가 숫자가 아닌 문자 인 경우,
        # return 0
        if len(str) == 0 or not str[0].isdigit():
            return 0

        # 문자열을 반복하고 숫자인 모든 문자를 추가
        for i, char in enumerate(str):
            if char.isdigit():
                answer += char
            else:
                break

        # integer로 변환
        answer = int(answer)

        return min(int_max, answer * sign) if sign > 0 else max(int_min, answer * sign)
