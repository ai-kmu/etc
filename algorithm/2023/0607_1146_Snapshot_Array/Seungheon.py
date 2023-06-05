# fail code - 수정중

class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.array = [0 for _ in range(length)]
        self.snap_id = -1
        self.snapshot_log = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snapshot_log.append(self.array.copy())
        self.snap_id += 1
        return self.snap_id  

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot_log[snap_id][index]
