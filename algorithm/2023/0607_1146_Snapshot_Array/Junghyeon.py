'''
get 부분이 어려워서 아직 구현중...
'''

class SnapshotArray:
    
    # 생성자 : 길이에 맞는 배열 생성
    def __init__(self, length):
        self.call = 0
        self.array = [0] * length
    
    # set : index에 val 값 저장
    def set(self, index, val):
        self.array[index] = val
    
    # (호출 횟수 - 1)을 반환
    def snap(self):
        self.call += 1
        return self.call - 1

    def get(self, index, snap_id):
