# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
      result=[]
      for i in range(nestedList):
        if nestedList[i].isInteger():
          result.append(nestedList[i].getInteger()) # 원소가 정수인 경우 result에 저장
        else:
          result.extend(nestedList[i].getList()) # 원소가 list인 경우 하나의 배열로 extend하여 result에 저장

      self.result = result # 결과 result 저장
      self.index=-1

    def next(self) -> int:
      return self.result[self.index]

    def hasNext(self) -> bool:
      self.index+=1
      if self.index<len(self.result) : # self.index가 result의 길이보다 작으면
        return True # True 출력
      else:
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
