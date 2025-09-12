# 풀다 실패.. 안풀어주셔도 됩니다

class Robot:

    def __init__(self, width: int, height: int):
        # define directions
        self.dirs_text = ["East", "North", "West", "South"]
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # init pose
        self.x = 0
        self.y = 0
        self.dir = 0

        # width, height
        self.size = (width, height)
        self.w = width - 1
        self.h = height - 1


    def step(self, num: int) -> None:
        rest_x, rest_y = 0, 0
        if self.dir % 2:
            rest_y = num
        else:
            rest_x = num

        # 최대 이동, 방향 전환, 남은거 최대 이동, 반복
        while True:
            dx, dy = self.dirs[self.dir]
            move_x, move_y = self.x + rest_x * dx, self.y + rest_y * dy
            self.x, self.y = min(self.w, move_x), min(self.h, move_y)
            rest_x, rest_y = move_x - self.x, move_y - self.y

            if rest_x or rest_y:
                self.dir = (self.dir + 1) % 4
                rest_x, rest_y = rest_y, rest_x
            
            else:
                break


    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        return self.dirs_text[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
