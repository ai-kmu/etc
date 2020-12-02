class NestedIterator(object):

    def __init__(self, nestedList):
        """
        자료 구조 초기화 하기.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        while nestedList:
            self.stack.append(nestedList.pop())

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()     

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
