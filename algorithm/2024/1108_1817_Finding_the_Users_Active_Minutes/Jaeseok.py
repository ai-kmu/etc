from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # answer의 길이는 무조건 k의 길이
        answer = [0] * k
        # unique한 minute을 담아야 하기 때문에 defaultdict 안에 담을 set을 선언
        users = defaultdict(set)
        # logs를 순회하면서 개별 유저가 어느 분에 활동했는지 기록
        for id, minute in logs:
            users[id].add(minute)
        # 각 user의 UAM을 계산 후 해당 UAM에 1을 더해주고 리턴
        for i in users:
            answer[len(users[i])-1] += 1
        return answer
        
