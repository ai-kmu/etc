

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def DFS(nestedList):
            if nestedList == None:
                return []
            ans = []
            for n in nestedList:
                if n.getInteger() is not None:
                    ans.append(n.getInteger())
                ans += DFS(n.getList()) 
            return ans
        self.idx = -1            
        self.ans = DFS(nestedList)
    def next(self) -> int:
        self.idx+=1
        return self.ans[self.idx]

    def hasNext(self) -> bool:
        return self.idx < len(self.ans) -1
