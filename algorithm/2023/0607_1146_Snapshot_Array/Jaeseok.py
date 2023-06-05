# time limit(67/74)...

from collections import defaultdict


class SnapshotArray:
    def __init__(self, length: int):
        self.arr = defaultdict(dict)
        self.arr[0] = defaultdict(int)
        self.length = length
        for i in range(self.length):
            self.arr[0][i] = 0
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.arr[self.snap_id] = defaultdict(int)
        for i in range(self.length):
            self.arr[self.snap_id][i] = self.arr[self.snap_id - 1][i]
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.arr[snap_id][index]
      
