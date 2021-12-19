class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 1차원 dp 배열을 선언, 이때 각 인덱스의 값은 bool값이므로 False로 초기화
        dp = [False]*(len(s)+1)
        dp[0] = True

        # p에 있는 캐릭터 p를 s의 캐릭터들과 비교하며 진행
        for cp in p:
            # curr의 초기 값을 정할 때, cp의 캐릭터를 보고 결정, 만약 *이면
            # dp의 처음에 있는 값으로 정하고 이외에는 False
            curr = [dp[0] if cp=='*' else False]
            f = curr[0]
            # 문자열 s를 enumerate를 통해 루프를 돌며 dp를 진행
            for i, cs in enumerate(s):
                f |= dp[i+1]
                # 만약 cp가 알파벳일 경우 해당 인덱스의 s의 캐릭터와 같을 때 curr에 True로 추가
                # 이때, dp안의 배열과 and 연산을 통해 둘 다 True인 경우만 curr에 True로 추가
                if cp.isalpha():
                    curr.append(s[i]==cp and dp[i])
                # 만약 cp가 ?일 경우 dp배열의 해당 인덱스만 curr에 추가
                elif cp == '?':
                    curr.append(dp[i])
                # 그 외의 경우는 f를 추가
                # f는 cp의 문자가 *일 때, 그 다음 인덱스와 or 연산을 한 값으로
                # *인 경우 f를 curr에 추가해줌
                else:
                    curr.append(f)
            # dp 연산이 끝난 후 dp를 curr로 바꿔줌
            dp = curr
        # 결과값으로는 dp의 마지막 값을 내보내줌
        return dp[-1]
        
