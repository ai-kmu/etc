class Robot:

    def __init__(self, width: int, height: int):
        self.pos = [0,0]
        self.dir = "East"
        self.width = width
        self.height = height

    def step(self, num: int) -> None:

        # 전체 길이 넘어가면(한바퀴) -> 다돌았다침
        num = num % (2*(self.width + self.height -2))
        # 제자리로 왔을 때, 코너라면 방향이 바뀜(실제로 이동했기때문에)
        if num == 0:
            if self.pos == [0,0]: #동
                self.dir = "South" #남
            elif self.pos == [self.width-1,0]: #북
                self.dir = "East" # 동
            elif self.pos == [0, self.height-1]: #남
                self.dir = "West" #서
            elif self.pos == [self.width-1,self.height-1]:#서
                self.dir = "North" #북
            return
        while num > 0:
            if self.dir in ("East","West"):
                if self.dir == "East":
                    if self.pos[0] < self.width-1:
                        self.pos = [a + b for a, b in zip(self.pos, [1,0])]
                    else:
                        self.dir = "North"
                        continue
                else:# West
                    if self.pos[0] > 0:
                        self.pos = [a + b for a, b in zip(self.pos, [-1,0])]
                    else:
                        self.dir = "South"
                        continue
            else:
                if self.dir == "North":
                    if self.pos[1] < self.height-1:
                        self.pos = [a + b for a, b in zip(self.pos, [0,1])]
                    else:
                        self.dir = "West"
                        continue
                else:
                    if self.pos[1] > 0:
                        self.pos = [a + b for a, b in zip(self.pos, [0,-1])]
                    else:
                        self.dir = "East"
                        continue
            num -= 1
        return

    def getPos(self) -> List[int]:
        return self.pos
        

    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
