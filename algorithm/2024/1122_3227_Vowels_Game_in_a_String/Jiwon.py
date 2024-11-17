class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0

        # s에 포함된 모음 개수 세기
        for char in s:
            if char in 'aeiou':
                cnt += 1
                
        # 모음이 없으면 무조건 alice가 짐
        if cnt is 0:
            return False
        # 홀수인 경우 무조건 alice가 이김 (첫 턴에 전부 제거)
        # 짝수인 경우에도 예제 1처럼 결국 alice가 이김
        return True
        
