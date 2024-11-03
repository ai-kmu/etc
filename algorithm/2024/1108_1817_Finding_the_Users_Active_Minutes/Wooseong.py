from collections import defaultdict as ddict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # user 별로 action한 time을 딕셔너리로 저장
        user_act_dict = ddict(set)
        for ID, time in logs:
            user_act_dict[ID].add(time)

        # user 별로 UAM 계산해서 answer update
        answer = [0 for _ in range(k)]
        for user, times in user_act_dict.items():
            UAM = len(times)
            # ddict로 해둬서 log에 없는 애들은 UAM이 0이 됨
            if UAM:
                answer[UAM - 1] += 1

        return answer
