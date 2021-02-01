class Solution:
    def minFlips(self, target: str) -> int:
        answer = 0
        for bulb in range(len(target)-1):              
            if target[bulb] + target[bulb+1] == '10':  # '10'이 나타나면 2번 뒤집어야 함
                answer += 1
        return answer*2 + int(target[-1])              # answer에 *2를 하고 마지막이 1인 경우에는 한번 더 뒤집어야 하고 0인 경우에는 안 뒤집어도 된다
