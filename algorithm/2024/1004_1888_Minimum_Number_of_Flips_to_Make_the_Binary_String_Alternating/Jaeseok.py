# time limit
# 모든 경우를 순회하면서 다시 count하기 때문인듯(O(N^2)
from collections import deque

class Solution:
    def minFlips(self, s: str) -> int:
        answer = 10 ** 5
        s = list(s)
        j = 0
        l = len(s)
        s = s if l % 2 == 0 else s + s
        while j < l:
            now, even_zero, odd_zero, even_one, odd_one = 0, 0, 0, 0, 0
            new_s = s[j:l + j]
            # print(new_s)
            odd_zero = new_s[1::2].count('0')
            odd_one = new_s[1::2].count('1')
            even_zero = new_s[::2].count('0')
            even_one = new_s[::2].count('1')
            now = min(odd_zero, even_zero) + min(odd_one, even_one)
            answer = min(answer, now)
            if l % 2 == 0:
                break
            j += 1

        return answer

# 답안 참조
# 짝수의 개수를 고려하여 O(n) 내로 문제를 해결할 수 있음
from collections import Counter

class Solution:
    def minFlips(self, s: str) -> int:

        # 0과 1의 개수를 Counter를 이용해서 셈
        even = Counter(s[::2])
        odd = Counter(s[1::2])

        # 2번째 연산을 해야 하는 경우의 수를 구하는 함수
        # 0이나 1이 모두 even하거나 odd한 경우에 alternative하므로 각 경우의 수 중 연산이 적은 쪽을 택함
        def get_min(even, odd):
            return min(even['0'] + odd['1'], even['1'] + odd['0'])
        
        answer = get_min(even, odd)

        # s의 길이가 짝수일 경우에 1번째 연산은 의미가 없음(첫번째 숫자를 마지막으로 보내도 짝수로 변하지 않음)
        if len(s) % 2 == 0:
            return answer
        # 그렇지 않은 경우에는 첫 번째 글자를 마지막으로 하나씩 보내면서 다시 2번째 연산을 계산
        else:
            for c in s:
                # 첫번째 숫자를 마지막으로 보내면 홀수가 되므로 counter에서 1을 빼줌
                # 이 연산이 진행되면 홀수의 개수와 짝수의 개수가 서로 맞바뀜
                # 첫번째 숫자를 고려하여 다시 짝수의 개수로 더해줌
                even[c] -= 1
                odd, even = even, odd
                even[c] += 1
                now = get_min(even, odd)
                answer = min(answer, now)
              
        return answer

            
