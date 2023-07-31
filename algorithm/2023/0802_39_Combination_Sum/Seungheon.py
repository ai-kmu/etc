class Solution(object):
    def combinationSum(self, candidates, target):
        # dp를 이용하여 target의 경우의 수 구하기
        # dp[idx] 에는 가능한 조합이 list로 들어있다.
        dp = [[[0]]] + [[] for i in range(target)]
        candidates.sort()

        # 1번째 칸부터 target번째 칸까지 채워가기
        for i in range(1, target+1):
            # 후보들을 이용하여 현재 값을 만들 수 있는지 확인
            for c_idx in candidates:
                cand_idx = i - c_idx
                if cand_idx >= 0:
                    for cand in dp[cand_idx]:
                        dp[i].append(tuple(sorted(list(cand) + [c_idx])))
                else:
                    break
            # 중복제거
            dp[i] = list(set(dp[i]))

        answer = []
        for v in dp[-1]:
            answer.append(v[1:])

        return answer


