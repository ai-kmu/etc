# Memory Limit Exceeded????

class SnapshotArray:
    def __init__(self, length: int):

        # SnapshotArray 저장 리스트 
        self.tmp = []
        # index, value 저장 dict
        self.dict = dict()
        self.idx = 0

    def set(self, index: int, val: int) -> None:
        self.dict[index] = val

    def snap(self) -> int:
        # 스냅샷 저장
        self.tmp.append(dict(self.dict))
        self.idx += 1
        return self.idx-1

    def get(self, index: int, snap_id: int) -> int:
        snap = self.tmp[snap_id] 
        if index in snap:
            return snap[index]
        else:
            return 0
