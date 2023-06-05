from collections import defaultdict
class SnapshotArray:
    # data는 딕셔너리 형태로 선언
    def __init__(self, length: int):
        self.data = defaultdict(defaultdict)
        self.snap_id = 0
    
    # index와 val을 입력 받아서 self.data의 요소값 세팅
    # 딕셔너리 안 딕셔너리 형태로 저장
    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val
    
    # snap()이 호출되면 snap_id 수 증가
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1
      
    # get(index, snap_id)가 호출되면 snap_id에 해당되는 index위치의 요소값 출력
    # snap_id for문을 역순으로 순회하면서 (이유: index마다 snapshot된 순간이 다르므로)
    # index 위치의 가장 큰 snap_id를 만나면 그 위치에 해당되는 data 값을 리턴
    # for문 순회 다 해도 없으면 0 리턴
    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id,-1,-1):
            if i in self.data[index]:
                return self.data[index][i]
        return 0
      
   '''
   - 풀면서 느낀점
  self.data를 어떤 형태로 선언하여 어떻게 저장하느냐에 따라 메모리 리밋이 나타남
  아래 코드와 같이 data 따로 snapshot을 따로하여 snapshot의 snap_id 위치에 따른 
  data를 따로 다 저장하면 메모리 초과 오류가 발생.
  그래서 위 코드처럼 데이터를 하나의 dict로 나타내어 dict 안에는 index 위치에 snap_id에 따른 값을
  따로 저장해야 함
   '''
  class SnapshotArray:

    def __init__(self, length: int):
        self.data = dict()
        self.snapshot = dict()
        self.snap_id = 0
        
    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        
    def snap(self) -> int:
        self.snapshot[self.snap_id] = dict(self.data)
        self.snap_id += 1
        return self.snap_id-1
        
    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id].get(index, 0)
