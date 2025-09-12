class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]  # 현재 위치 (x, y)
        
        # 로봇 반시계 방향으로 회전 -> 이동 경로 시계방향
        self.path = []
        for x in range(width):
            self.path.append([x, 0])  # 아래쪽
        for y in range(1, height):
            self.path.append([width - 1, y])  # 오른쪽
        for x in range(1, width):
            self.path.append([width - 1 - x, height - 1])  # 위쪽
        for y in range(1, height - 1):
            self.path.append([0, height - 1 - y])  # 왼쪽
        
        self.init = True  # 초기상태

    def step(self, num: int) -> None:
        cur_idx = self.path.index(self.pos)  # 현재 위치의 인덱스
        total = len(self.path)
        self.pos = self.path[(cur_idx + num) % total]  # 모듈러 연산으로 순환 이동
        self.init = False

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        # 초기 방향 무조건 동쪽
        if self.init:
            return "East"
        
        x, y = self.pos
        if x == 0:
            return "West" if y == self.height - 1 else "South"
        if x == self.width - 1:
            return "East" if y == 0 else "North"
        if y == 0:
            return "East"
        return "West"

        
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
