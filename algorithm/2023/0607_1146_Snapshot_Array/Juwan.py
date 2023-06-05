#  Memory Limit 나서 개선 중

from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        
        self.arr = [0] * length
        self.snap_dict = {0 : self.arr}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_dict[self.snap_id] = self.arr
        self.snap_id = self.snap_id + 1

    def get(self, index: int, snap_id: int) -> int:
        
        return self.snap_dict[snap_id][index]
      
      
