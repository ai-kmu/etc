# 솔루션 참고

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def is_connected(a,b):
            x1, y1, r1 = bombs[a]
            x2, y2, r2 = bombs[b]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return dist <= r1


        conn = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    if is_connected(i,j):
                        conn[i].append(j)

        q = collections.deque()
        maxCount = float('-inf')

        for node in range(len(bombs)):
            if conn[node]:
                q.append(node)
                visited = set()
                visited.add(node)
                count = 0
                while q:
                    curr = q.popleft()
                    count+=1
                    maxCount = max(maxCount, count)
                    for child in conn[curr]:
                        if child not in visited:
                            visited.add(child)
                            q.append(child)

        return maxCount if maxCount != float('-inf') else 1
