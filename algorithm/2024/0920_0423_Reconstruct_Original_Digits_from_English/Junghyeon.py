from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)

        result = ''
        count = [0] * 10

        # 유일 문자 계산
        count[0] = cnt['z']
        count[2] = cnt['w']
        count[4] = cnt['u']
        count[6] = cnt['x']
        count[8] = cnt['g']

        # 겹치는 문자 제거
        count[1] = cnt['o'] - (count[0] + count[2] + count[4])
        count[3] = cnt['t'] - (count[2] + count[8])
        count[5] = cnt['f'] - count[4]
        count[7] = cnt['s'] - count[6]
        count[9] = cnt['i'] - (count[5] + count[6] + count[8])

        for idx, i in enumerate(count):
            result += i*str(idx)

        return result
