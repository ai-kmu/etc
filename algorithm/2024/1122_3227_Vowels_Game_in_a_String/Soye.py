class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # 모음 리스트 정의
        vovel_list = ['a', 'e', 'i', 'o', 'u']
        vovel = 0  # 모음의 개수를 저장할 변수
        
        # s를 순회하면서 모음인지 확인
        for ch in s:
            if ch in vovel_list:  # 현재 문자가 모음 리스트에 포함되어 있으면
                vovel += 1  # 모음 개수를 증가

        # 모음의 개수가 0이라면, Alice는 아무 행동도 할 수 없으므로 Bob이 승리
        if vovel == 0:
            return False

        # 모음이 하나라도 있다면 Alice가 승리
        return True
