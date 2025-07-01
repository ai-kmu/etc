# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # 뜯어본 결과 (`dir(iterator)`) `index`는 처음에 `0`으로 시작,
        # `next`는 현재 `index` 원소를 호출 후에 `index += 1`을 진행
        # 따라서 "다음 원소"는 `index` 자체를 호출하면 됨
        # 그리고 `nums`는 `v`로 저장해 둠
        return self.iterator.v[self.iterator.index]
        

    def next(self):
        """
        :rtype: int
        """
        # 기존 Iterator 클래스에 있는 메서드 그대로 사용하기
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # 기존 Iterator 클래스에 있는 메서드 그대로 사용하기
        return self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
