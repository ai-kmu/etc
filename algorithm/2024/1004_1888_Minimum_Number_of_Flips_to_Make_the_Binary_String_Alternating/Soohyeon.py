# 솔루션 참조

class Solution:
    def minFlips(self, s):
        
        n = len(s)  # 주어진 문자열 s의 길이를 저장
        cp = s + s  # 문자열 s를 두 번 이어붙여 cp라는 새로운 문자열 생성 (원형 문자열을 다루기 위해)
        
        # 두 가지 대안 패턴을 만듦:
        # s1: '1010...' 패턴
        # s2: '0101...' 패턴
        s1 = ""
        s2 = ""
        for i in range(len(cp)):
            if i % 2 == 0:  # 짝수 인덱스에 '1' 또는 '0'을 넣음
                s1 += '1'
                s2 += '0'
            else:  # 홀수 인덱스에 '0' 또는 '1'을 넣음
                s1 += '0'
                s2 += '1'
        
        # res1: s1 패턴과의 차이
        # res2: s2 패턴과의 차이
        res1 = 0  # 현재까지의 s1 패턴과의 차이를 계산할 변수
        res2 = 0  # 현재까지의 s2 패턴과의 차이를 계산할 변수
        
        res = 10**6  # 최소 변환 횟수를 저장할 변수 (아주 큰 수로 초기화)
        
        # 슬라이딩 윈도우 기법을 사용해 cp에서 길이 n의 모든 부분 문자열을 탐색
        for i in range(len(cp)):
            # cp의 현재 인덱스 i에서 s1 패턴과 다르면 res1 증가
            if cp[i] != s1[i]:
                res1 += 1
            # cp의 현재 인덱스 i에서 s2 패턴과 다르면 res2 증가
            if cp[i] != s2[i]:
                res2 += 1
            
            # 슬라이딩 윈도우가 원래 문자열의 크기(n)를 초과한 경우, 윈도우의 시작 부분에서 res1, res2를 조정
            if i >= n:
                # 슬라이딩 윈도우에서 벗어나는 부분을 다시 맞춰줌
                if cp[i - n] != s1[i - n]:
                    res1 -= 1
                if cp[i - n] != s2[i - n]:
                    res2 -= 1
            
            # 슬라이딩 윈도우의 크기가 n에 도달하면, 최소값 업데이트
            if i >= n - 1:
                res = min(res, res1, res2)
        
        return res  # 최소 변환 횟수를 반환