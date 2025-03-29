class Solution:
    # union-find algorithm
    def find(self, a):
        if self.parent[a] == a:
            return a
        return self.find(self.parent[a])

    def union(self, a, b):
        i = self.find(a)
        j = self.find(b)
        if i < j:
            self.parent[j] = i
        else:
            self.parent[i] = j

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.parent = list(range(len(isConnected)))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union(i,j)  # 연결되었다면 union
        cnt = dict()
        for i in self.parent:
            cnt[self.find(i)] = True  # find()가 같은 city끼리는 직접적으로 연결되어있음

        return len(cnt.keys())
