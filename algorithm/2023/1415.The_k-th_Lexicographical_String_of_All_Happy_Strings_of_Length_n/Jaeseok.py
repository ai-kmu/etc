from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.happy = []
        self.next_strings = ["a", "b", "c"]
        # BFS
        q = deque()
        # 맨 처음 문자는 무조건 3가지 경우의 수만 존재
        q.append(("a", 1))
        q.append(("b", 1))
        q.append(("c", 1))
        
        while q:
            # s: 현재까지 만들어진 string, l: 현재 길이
            s, l = q.popleft()
            # 최대 길이에 도달하면 happy string에 저장
            if l == n:
                self.happy.append(s)
                continue
            # 마지막 글자 제외한 나머지 글자를 더해서 큐에 추가
            for n_s in self.next_strings:
                if s[-1] != n_s:
                    q.append((s+n_s, l+1))

        # k가 만들어진 happy string의 길이보다 짧으면 happy string을 sort한 뒤 k 자리의 string 반환, 아니라면 "" 반환
        return sorted(self.happy)[k-1] if k <= len(self.happy) else ""
            
