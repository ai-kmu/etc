class Solution:
    def backtrack(self, n, idx, visited):
        if idx > n:
            self.num_of_beauties += 1
            return
        
        for i in range(1, n + 1):
            # i가 idx로 나누어 떨어지거나, idx가 i로 나누어 떨어져야 함
            if not visited[i] and (i % idx == 0 or idx % i == 0):
                visited[i] = True

                self.backtrack(n, idx + 1, visited)

                visited[i] = False
  
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        self.num_of_beauties = 0

        self.backtrack(n, 1, visited)

        return self.num_of_beauties
