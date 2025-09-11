class Robot:

    def __init__(self, width: int, height: int):
        self.lapSquare = 0
        self.lap = 2 * (width + height - 2)
        self.width = width - 1
        self.height = height - 1
        self.init = True

    def step(self, num: int) -> None:
        self.lapSquare = (self.lapSquare + num) % self.lap
        self.init = False

    def getPos(self) -> List[int]:
        if self.lapSquare <= self.width:
            return [self.lapSquare, 0]
        if self.lapSquare <= self.width + self.height:
            return [self.width, self.lapSquare - self.width]
        if self.lapSquare <= 2 * self.width + self.height:
            return [2 * self.width + self.height - self.lapSquare, self.height]
        return [0, self.lap - self.lapSquare]
        
    def getDir(self) -> str:
        if self.lapSquare == 0 and not self.init:
            return "South"
        if 0 <= self.lapSquare <= self.width:
            return "East"
        if self.lapSquare <= self.width + self.height:
            return "North"
        if self.lapSquare <= 2 * self.width + self.height:
            return "West"
        return "South"
