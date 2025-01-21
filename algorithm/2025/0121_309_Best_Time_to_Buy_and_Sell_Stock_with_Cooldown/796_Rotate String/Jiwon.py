class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        goal = list(goal)
        q = deque(s)

        for i in range(len(s)):
            q.append(q.popleft())
            if list(q) == goal:
                return True
        return False
        
