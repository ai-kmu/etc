from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.array = [{"snap_ids": [-1], "vals": [0]} for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index]["snap_ids"].append(self.snap_id)
        self.array[index]["vals"].append(val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        return self.array[index]["vals"][bisect_right(self.array[index]["snap_ids"], snap_id)-1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
