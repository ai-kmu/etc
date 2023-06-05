# 아직 timeout,, 더 풀어볼 예정

from copy import deepcopy

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [0 for _ in range(length)]
        self.snap_id = -1
        self.snapshot = {self.snap_id: deepcopy(self.array)}
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index] = val
        

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        self.snapshot[self.snap_id] = deepcopy(self.array)
        return self.snap_id
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        return self.snapshot[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
