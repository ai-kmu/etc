from collections import defaultdict
from functools import lru_cache

class SnapshotArray:

    def __init__(self, length: int):
        
        self.snap_dict = defaultdict(int)
        self.snap_id = 0

        self.mapp = defaultdict(int)
        self.map_id = -1

        self.arr = {}

    def set(self, index: int, val: int) -> None: 
        self.snap_dict[index] = val

    @lru_cache
    def snap(self) -> int:

        self.snap_id += 1

        if self.snap_id > 1 and self.arr[self.mapp[self.snap_id - 1]].items() == self.snap_dict.items():
            self.mapp[self.snap_id] = self.map_id
        else:
            self.map_id += 1
            self.mapp[self.snap_id] = self.map_id
            self.arr[self.mapp[self.snap_id]] = self.snap_dict.copy()

        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        
        # print(self.arr)

        return self.arr[self.mapp[snap_id + 1]][index]


