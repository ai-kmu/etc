# memory limit error
# class SnapshotArray:
#     def __init__(self, length: int):
#         self.array = [0 for _ in range(length)]
#         self.snap_dict = dict()
#         self.snap_id = -1

#     def set(self, index: int, val: int) -> None:
#         self.array[index] = val
        
#     def snap(self) -> int:
#         self.snap_id += 1
#         for key, value in self.snap_dict.items():
#             if value == self.array:
#                 self.snap_dict[self.snap_id] = self.snap_dict[key]
#                 return self.snap_id

#         self.snap_dict[self.snap_id] = self.array[:]
#         return self.snap_id

#     def get(self, index: int, snap_id: int) -> int:
#         return self.snap_dict[snap_id][index]
        
# 이진 탐색
class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [[(0, 0)] for _ in range(length)]  

    def set(self, index: int, val: int) -> None:
        # index 위치의 배열 값에 (snap_id, val) 형태로 추가
        self.array[index].append((self.snap_id, val))  

    def snap(self) -> int:
        self.snap_id += 1  
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # index 위치의 배열 값의 스냅샷들을 가져옴
        snapshots = self.array[index]  

        # 이진 탐색을 사용하여 snap_id와 가장 가까운 스냅샷을 찾음
        left, right = 0, len(snapshots) - 1
        while left <= right:
            mid = (left + right) // 2
            if snapshots[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        # 가장 가까운 스냅샷의 값 반환
        return snapshots[right][1]
