class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # 모음 개수가 0개가 아닌 이상 항상 Alice가 이김
        # 1. 모음 개수 : Odd -> Alice가 한 번에 모두 가져감
        # 2. 모음 개수 : Even -> Alice는 자신의 차례 두 번에서 Odd를 가져가 Even의 모음 개수를 가져감
        vowel_cnt = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

        return vowel_cnt != 0
