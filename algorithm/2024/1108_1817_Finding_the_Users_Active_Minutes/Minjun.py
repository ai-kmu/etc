class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = {}
        l = [0 for i in range(k)]
        for uid, m in logs:
            if uid not in d:
                d[uid] = set()
            d[uid].add(m)
        for i in d.values():
            if i:
                l[len(i)-1] += 1
        return l
