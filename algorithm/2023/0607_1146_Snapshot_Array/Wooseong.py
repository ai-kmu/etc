class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = {}

        # snap만 주구장창하는 경우에 OOM이 난 거에서 힌트 -> set을 몇 번 했는지를 확인
        self.num_set = 0
        self.snap_id = 0
        self.snaps = {-1: -1}  # snap_id: num_set
        self.snapshot = {}  # "num_set"에 대해서 snapshot 저장

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # set을 호출할 때마다 값 저장
        self.array[index] = val
        self.num_set += 1
        

    def snap(self):
        """
        :rtype: int
        """
        # 현 snap_id를 set 호출 횟수와 연결
        self.snaps[self.snap_id] = self.num_set

        # 새로 set == 이전 snap_id와 value가 다름 -> 이때만 copy
        if self.snaps[self.snap_id] != self.snaps[self.snap_id - 1]:
            self.snapshot[self.num_set] = dict(self.array)  # snaps의 value를 이용해서 get할 거임

        # snap_id 올리고 return은 올리기 전의 값(호출 시의 값)
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        
        # snap_id에 해당하는 num_set으로 snapshot 호출
        return self.snapshot[self.snaps[snap_id]].get(index, 0)
