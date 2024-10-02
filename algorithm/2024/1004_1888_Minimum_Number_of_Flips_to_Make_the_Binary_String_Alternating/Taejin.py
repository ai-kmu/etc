# 풀지 못하여 솔루션 봤습니다..
class Solution:
    def minFlips(self, s: str) -> int:
        # 짝수 인덱스 0, 홀수 인덱스 1인 경우에서 올바른 수
        cnt0 = s[::2].count('0') + s[1::2].count('1')
        # 짝수 인덱스 1, 홀수 인덱스 0인 경우에서 올바른 수
        cnt1 = len(s) - cnt0
        ans = min(cnt0, cnt1) # 두 경우 중 작은 경우부터 시작
        if not len(s) % 2:
            return ans
        
        # 문자 탐색
        for n in s:
            cnt0, cnt1 = cnt1, cnt0 # type1 operation
            
            # type2 operation
            if n == '1': # 1이 나오면 1 증가, 0감소
                cnt1 += 1
                cnt0 -= 1
            else: # 0이 나오면 0증가, 1감소
                cnt0 += 1
                cnt1 -= 1
            
            #그 중 최솟값(플립 횟수)을 ans에 저장
            ans = min(cnt0, cnt1, ans) 
        return ans

            
