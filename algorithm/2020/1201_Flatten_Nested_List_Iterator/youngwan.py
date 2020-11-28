class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def check(nestedList):                                  # NestedList를 하나의 list로 바꾸는 함수
            temp = []
            for num in range(len(nestedList)):                  # nestedList를 돌면서
                if nestedList[num].isInteger():                 # 하나의 단일 정수이면 
                    temp.append(nestedList[num].getInteger())   # 리스트에 저장
                else:                                           # nestelist인 경우
                    temp += check(nestedList[num].getList())    # nestedlist를 하나의 리스트로 변환해주는 함수 
            return temp
        
        self.i = -1 
        self.nested = check(nestedList)                          # 하나의 리스트로 저장

    def next(self) -> int:                                       # 다음 원소 반환
        return self.nested[self.i]
    
    def hasNext(self) -> bool:                                   # 다음 원소가 없는 경우 False 반환
        self.i += 1
        if(self.i < len(self.nested)):
            return True
        else:
            return False
