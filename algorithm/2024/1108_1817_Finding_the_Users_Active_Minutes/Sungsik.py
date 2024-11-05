from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes = defaultdict(set)

        # 각 log마다 minute을 set에 추가
        for uid, minute in logs:
            minutes[uid].add(minute)
        
        answer = [0] * k
        # 각 user마다 uam을 추가
        for _, user_minutes in minutes.items():
            answer[len(list(user_minutes))-1] += 1
        
        return answer
