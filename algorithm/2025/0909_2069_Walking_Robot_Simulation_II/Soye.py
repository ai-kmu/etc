class Robot:
    def __init__(self, width: int, height: int):
        # 격자 크기
        self.width = width
        self.height = height
        
        # 방향 순서 (동 → 북 → 서 → 남, 반시계 방향 회전)
        self.dirs = ["East", "North", "West", "South"]
        self.dir_idx = 0  # 초기 방향 East
        
        # 로봇 위치
        self.x, self.y = 0, 0
        
        # 경로의 총 길이 (사각형 둘레 - 4)
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return  # width=1 또는 height=1일 때 예외
        
        # num을 전체 경로 길이로 나눠주면 반복되는 경로 최적화
        num %= self.perimeter
        if num == 0:
            # 한 바퀴 끝났을 때의 방향 보정
            if self.x == 0 and self.y == 0:
                self.dir_idx = 3  # South
            elif self.x == self.width - 1 and self.y == 0:
                self.dir_idx = 0  # East
            elif self.x == self.width - 1 and self.y == self.height - 1:
                self.dir_idx = 1  # North
            elif self.x == 0 and self.y == self.height - 1:
                self.dir_idx = 2  # West
            return
        
        # 남은 이동 처리
        while num > 0:
            if self.dir_idx == 0:  # East
                step = min(num, self.width - 1 - self.x)
                self.x += step
            elif self.dir_idx == 1:  # North
                step = min(num, self.height - 1 - self.y)
                self.y += step
            elif self.dir_idx == 2:  # West
                step = min(num, self.x)
                self.x -= step
            else:  # South
                step = min(num, self.y)
                self.y -= step
            
            num -= step
            if num > 0:  # 벽에 부딪히면 반시계 회전
                self.dir_idx = (self.dir_idx + 1) % 4

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dirs[self.dir_idx]
