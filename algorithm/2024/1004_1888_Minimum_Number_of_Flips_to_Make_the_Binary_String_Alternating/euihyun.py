# 풀이 실패, 리뷰 안해주셔도 됩니다

class Solution:
    def minFlips(self, s: str) -> int:
            # 최소 뒤집기 횟수 저장 
            minimumFlips = len(s)
            
            # 윈도우 크기 설정
            k = len(s)
            
            # 문자열 길이가 홀수인 경우, 문자열을 두 배로 늘림
            # 이렇게 하면 Type-1 연산(문자열의 첫 번째 문자를 끝으로 보내기)을 수동으로 수행할 필요가 없음
            s = s if k % 2 == 0 else s + s
            
            # 이진수로 만들 수 있는 문자열은 두 가지뿐임 0,1 시작
            altArr1, altArr2 = [], []        
            for i in range(len(s)):
                altArr1.append("0" if i % 2 == 0 else "1")
                altArr2.append("1" if i % 2 == 0 else "0")
                
            alt1 = "".join(altArr1)
            alt2 = "".join(altArr2)
            
            
            
            diff1, diff2 = 0, 0
            
            i, j = 0, 0
            
            while j < len(s):
                # 현재 문자가 교대 문자열(alt1, alt2)과 다르면 차이를 증가시킴
                if s[j] != alt1[j]: diff1 += 1
                if s[j] != alt2[j]: diff2 += 1
                    
                # 윈도우 크기가 아직 원하는 길이에 도달하지 않았으면 j를 증가
                if j - i + 1 < k: 
                    j += 1
                else:
                    # 최소 뒤집기 횟수 갱신
                    minimumFlips = min(minimumFlips, diff1, diff2)
                    # 윈도우의 시작 부분에 있는 문자와 교대 문자열의 차이를 감소시킴
                    if s[i] != alt1[i]: diff1 -= 1
                    if s[i] != alt2[i]: diff2 -= 1
                    # 윈도우를 오른쪽으로 이동
                    i += 1
                    j += 1
            
            return minimumFlips
