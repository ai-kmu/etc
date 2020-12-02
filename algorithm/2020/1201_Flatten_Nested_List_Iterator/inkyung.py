class NestedIterator(object):
    def __init__(self,nestedList):
        self.queue = collections.deque([])
        for num in nestedList:
            # 들어 있는 값이 숫자이면 그대로 que에 넣고
            if num.isInteger():
                self.queue.append(num.getInteger())
            else:
                # 들어 있는 값이 리스트이면 이터레이션을 돌면서 숫자 하나씩 왼쪽부터 꺼내서 집어넣어야 함
                got_list = NestedIterator(num.getList())
                while got_list.hasNext():
                    self.queue.append(got_list.next())

    def hasNext(self):
        # 리스트 안의 값이 계속 있는지 없는지
        if self.queue:
            return True
        return False
    def next(self):
        # 리스트에 값이 남아 있으면 왼쪽부터 가져오고 지우기
        return self.queue.popleft()
         
