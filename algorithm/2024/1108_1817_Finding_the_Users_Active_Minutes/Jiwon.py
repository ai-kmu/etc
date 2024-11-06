class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        set_logs = defaultdict(set)
        ans = [0] * k

        # UAM 확인
        for user, time in logs:
            set_logs[user].add(time)
        
        # UAM에 맞게 정답리스트 카운팅
        for uam in set_logs.values():
            ans[len(uam) - 1] += 1

        return ans
