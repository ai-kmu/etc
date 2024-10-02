# 솔루션 참고: 슬라이딩 윈도우 사용
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/solutions/1254138/python-easy-sliding-window-based-solutiion

class Solution(object):
    def minFlips(self, s):
        n = len(s)  # 문자열의 길이를 저장 > 윈도우의 길이
        s += s  # 문자열을 두 배로 확장하여 회전된 문자열의 모든 경우를 처리 가능하게 함

        ans = sys.maxsize
        ans1, ans2 = 0, 0  # 1로/0으로 시작하는 문자열을 만들기 위한 변경 횟수

        s1 = "10" * ((len(s) + 1) // 2)  # 1로 시작하는 패턴 생성
        s2 = "01" * ((len(s) + 1) // 2)  # 0으로 시작하는 패턴 생성

        # n이 홀수인 경우 길이를 맞춰서 s1과 s2를 슬라이싱
        s1 = s1[:len(s)]
        s2 = s2[:len(s)]

        for i in range(len(s)):
            if s[i] != s1[i]:  # 일치하지 않으면 변경이 필요하므로 ans1을 1 증가
                ans1 += 1
            if s[i] != s2[i]:  # 일치하지 않으면 변경이 필요하므로 ans2를 1 증가
                ans2 += 1
            
            if i >= n:
                # 윈도우의 길이가 n을 넘어서면 제외된 문자를 원상태로 되돌려야 함
                # 제외된 문자가 변경되었으면 그 변경을 취소
                if s[i - n] != s1[i - n]:
                    ans1 -= 1
                if s[i - n] != s2[i - n]:
                    ans2 -= 1
            if i >= n - 1:
                # 윈도우의 길이가 n이 된 시점부터 최소 변경 횟수를 갱신
                ans = min([ans, ans1, ans2])
        return ans
