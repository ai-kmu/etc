# 최종 `s`는 다음 두 종류
# case1. 홀수 idx에 0, 짝수 idx에 1
# case2. 홀수 idx에 1, 짝수 idx에 0
# 이걸 반대로 세서, 0으로 만들면 됨. 즉,
# case1 == {짝수 idx ([::2])의 0 개수} + {홀수 idx ([1::2])의 1 개수} = 0
# case2 == {짝수 idx ([::2])의 1 개수} + {홀수 idx ([1::2])의 o 개수} = 0
# 하지만 `s`의 길이가 홀수면, "Type-1" operation을 통해 패턴이 바뀜
# 따라서 모든 패턴을 확인해봐야함

class Solution:
    def minFlips(self, s: str) -> int:
        # 현재 s가 어떤 케이스에 속하는지 확인
        case1 = s[::2].count('0') + s[1::2].count('1')
        case2 = len(s) - case1
        
        # 작게 어긋난 쪽으로 Type-2 operation 하는 게 정답
        answer = min(case1, case2)
        
        # 짝수면 가능한 pattern이 하나임
        if not (len(s) % 2):
            return answer

        # 홀수면 Type-1 operation을 통해 pattern이 바뀜
        for num in s:
            # Type-1 operation을 하면 홀짝 idx가 뒤바뀜
            case1, case2 = case2, case1
            
            # 맨 앞 (짝수 idx)에 있던 걸 맨 뒤 (홀수 idx)로 넘기는 과정
            # 1은 case1에서 빼야 되고, 0은 더해줘야함
            case1, case2 = (case1 - 1, case2 + 1) if num == "1" else (case1 + 1, case2 - 1)
            
            # 정답 갱신
            answer = min(case1, case2, answer)
            
            # 조금이라도 빠르게 해보려는 발악
            if answer == 0:
                return answer

        return answer
