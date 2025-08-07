class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rung = 0  # 추가
        prev = 0  # 이전
        
        for current in rungs:
            if current - prev > dist:  # 발판 설치해야함
                tmp = (current - prev - 1) // dist
                rung += tmp
            prev = current
        
        return rung
