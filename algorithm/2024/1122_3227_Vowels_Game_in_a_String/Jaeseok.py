# 1. naive한 풀이방법(최초 시도)
# alice의 턴일 때 count가 1인 상태에서 끝나면 alice의 승리
# alice의 턴일 때 count가 0인 상태에서 끝나면 bob의 승리
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        turn = 1
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while True:
            # alice's turn
            if turn == 1:
                for i, v in enumerate(s):
                    if v in vowels:
                        if count == 1:
                            s = s[i:]
                            break
                        else:
                            count += 1
                else:
                    if count == 1:
                        return True
                    else:
                        return False
            # bob's turn
            else:
                for i, v in enumerate(s):
                    if v in vowels:
                        s = s[i:]
                        break
            count = 0
            turn *= -1

# 2. 빠른 풀이
# 모음이 하나라도 있으면 무조건 alice의 승리, 하나도 없으면 bob의 승리가 됨
 class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in vowels:
            if i in s:
                return True
        else:
            return False
