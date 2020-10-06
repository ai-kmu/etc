## S[nums]를 nums만큼의 돈을 채우기 위한 동전의 최소값이라 가정하자
## 그리고 coins에 내가 가지고 있는 coin의 종류가 저장되어있다고 가정하자 
## 우선 첫항은 S[0] = 0이다.
## 그리고 S[nums] = min([S[nums] - coin for coin in coins])이다.
## 이를 동적 계획법으로 풀면 된다.

class Solution:
    def coinChange(self, coins, amount):
        ans = [0]
        for i in range(1, amount+1):
            temp_ans = []
            for j in coins:
                if i - j>=0 and ans[i-j]>=0:
                    temp_ans.append(ans[i-j] + 1)
            if len(temp_ans)>0:
                ans.append(min(temp_ans))
            else:
                ans.append(-1)
        return ans[amount]
