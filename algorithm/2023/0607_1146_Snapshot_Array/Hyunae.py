class SnapshotArray:

    def __init__(self, length: int):
        # {snap_id: value}
        self.arr = [[] for _ in range(3)]
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        # self.arr[index].append({self.snap_id: val})
        if len(self.arr[index]):
            self.arr[index][0][self.snap_id] = val
        else:
            self.arr[index].append({self.snap_id: val})
        # print(self.arr[index][0])
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        # index out of range :(
        return self.arr[index][0][snap_id-1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
