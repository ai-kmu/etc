# 못풀어서 정답 봤어요 뭔가 쉬우면서 어렵네요

class SnapshotArray:
    def __init__(self, length):
        self.length = length
        # (스냅샷 ID, 값) 형태의 튜플을 원소로 가지는 리스트로 초기화
        self.array = [[(0, 0)] for _ in range(length)]  
        self.snap_id = 0

    def set(self, index, val):
        # 배열의 index 위치에 (스냅샷 ID, 값)을 추가
        self.array[index].append((self.snap_id, val))  

    def snap(self):
        # 스냅샷 ID를 1 증가
        self.snap_id += 1
        # 현재 스냅샷 ID를 반환
        return self.snap_id - 1  

    def get(self, index, snap_id):
        # index 위치의 스냅샷들을 가져옴    
        snapshots = self.array[index]  

        # 이진 탐색을 사용하여 snap_id에 해당하는 스냅샷을 찾기.
        left, right = 0, len(snapshots) - 1
        while left <= right:
            mid = (left + right) // 2
            # mid 위치의 스냅샷의 ID가 snap_id보다 작거나 같은 경우
            # mid 다음 스냅샷의 ID가 snap_id보다 큰 경우
            # mid 위치의 스냅샷의 값 반환
            if snapshots[mid][0] <= snap_id:  
                if mid == len(snapshots) - 1 or snapshots[mid + 1][0] > snap_id: 
                    return snapshots[mid][1]  
                else:
                    left = mid + 1  
            else:
                right = mid - 1  
