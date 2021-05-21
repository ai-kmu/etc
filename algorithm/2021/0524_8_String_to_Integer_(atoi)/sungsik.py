class Solution:
    def myAtoi(self, s: str) -> int:
        # leading whitespace를 무시
        # 뒷부분 whitespace도 제거하지만 영향 없음
        s = s.strip()

        # strip한 결과 string이 빈 문자열이면 0을 리턴
        if len(s) == 0:
            return 0

        # 기본 부호를 +로 설정
        positive = True
        answer = 0

        # 앞에 부호가 있을 경우
        # 부호를 반영하고 제외시킨다.
        if s[0] == '-':
            positive = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # 문자열을 돌면서 숫자일경우 추가시키고 아닐경우 바로 break한다.
        for i in range(len(s)):
            if '0' <= s[i] and s[i] <= '9':
                answer = answer * 10 + int(s[i])
            else:
                # 첫번째 index부터 숫자가 아닐경우 바로 0을 리턴한다.
                if i == 0:
                    return 0
                break
        # 2진수로 변환한 값의 길이가 int 최대보다 길 경우
        # 부호에 따라 최댓값이나 최솟값을 리턴한다.
        # 33 = len(bin(2**31 - 1))
        if len(bin(answer)) > 33:
            if positive:
                return 2 ** 31 - 1
            else:
                return -2 ** 31
        return answer if positive else -answer