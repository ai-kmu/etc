class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def generateNestedList(nestedList): #nestedList 입력받아서 재귀 형태로 원소 저장
            ans=[]
            
            for element in nestedList:
                if element.isInteger(): # 그냥 숫자라면
                    ans.append(element.getInteger())
                else: #list라면
                    ans+=generateNestedList(element.getList()) # 재귀형태로 호출
                        
            return ans
        
        self.idx=-1 
        self.ans=generateNestedList(nestedList)
    
    def next(self) -> int: #다음 원소 반환
        self.idx+=1
        return self.ans[self.idx]
        
    
    def hasNext(self) -> bool: # 다음 원소가 있는지 확인 
        return self.idx<len(self.ans)-1
         
