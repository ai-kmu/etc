class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.content = nestedList[::-1]                 # 역순으로 초기화
        
    def next(self) -> int:
        get = self.content[-1].getInteger()             # 다음 것 뱉고 지우기
        del self.content[-1]
        return get
    
    def hasNext(self) -> bool:
        if len(self.content)==0:                        # 남아있는지 확인
            return False
        
        while self.content[-1].isInteger()==False:      # nestedList 다 풀기
            temp = self.content[-1].getList()
            del self.content[-1]
            self.content += temp[::-1]
            if len(self.content)==0:                    # while문 안에서도 list 내용물 남아있는지 확인
                return False
        return True
