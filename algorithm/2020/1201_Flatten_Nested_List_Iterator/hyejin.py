class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iterator_list = [] #가지고 있을 list
        for i in nestedList:
            if i.isInteger():
                self.iterator_list.append(i.getInteger())
            else:
                self.iterator_list += self.resolve(i)
        self.curr_idx = 0 # 현재 index
        
            
    # nestedInteger의 List를 재귀적으로 풀어줌
    def resolve(self, nestedList):
        temp_list = []
        for i in nestedList.getList():
            if i.isInteger():
                temp_list.append(i.getInteger())
            else:
                temp_list += self.resolve(i)
        return temp_list
        
        
    def next(self) -> int: # 현재 인덱스의 값을 return
        self.curr_idx += 1
        return self.iterator_list[self.curr_idx-1]
        
        
    def hasNext(self) -> bool: # 다음이 있나 확인
        return len(self.iterator_list) > self.curr_idx
