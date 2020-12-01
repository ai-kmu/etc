class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.idx = -1
        
        def makeNestedList(nestedList):  
            answer = []
            for n in nestedList:
                if n.isInteger():  # 정수인 경우 정답에 추가
                    answer.append(n.getInteger())  
                else:                      
                    answer.extend(makeNestedList(n.getList())) # 리스트 가져와서 재귀
                print(answer)
            return answer
        
        self.answer = makeNestedList(nestedList) # 정답 저장

    def next(self) -> int:     
        return self.answer[self.idx]
    
    def hasNext(self) -> bool:    # 다음 원소가 없는 경우 False 반환
        self.idx += 1
        return self.idx < len(self.answer)
