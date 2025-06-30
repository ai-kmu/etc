class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.value = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.value

    def next(self):
        """
        :rtype: int
        """
        return_value = self.value
        self.value = self.iterator.next()
        return return_value
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.value != -100000
