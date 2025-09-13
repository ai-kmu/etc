from typing import List

DIR_LIST = [[1, 0], [0, 1], [-1, 0], [0, -1]]

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cur_pos = [0, 0]
        self.cur_dir_idx = 0
        self.cur_dir = DIR_LIST[0]
        

    def step(self, num: int) -> None:
        if num == 0:
            return

        perimeter = 2 * (self.width - 1) + 2 * (self.height - 1)
        if perimeter == 0:
            return
            
        num %= perimeter
        if num == 0:
            if self.cur_pos == [0, 0] and self.cur_dir_idx == 0:
                self.cur_dir_idx = 3
                self.cur_dir = DIR_LIST[3]
            return

        while num > 0:
            if self.cur_dir_idx == 0:
                steps_possible = self.width - 1 - self.cur_pos[0]
                move = min(num, steps_possible)
                self.cur_pos[0] += move
                num -= move
                if num > 0:
                    self.cur_dir_idx = 1
            elif self.cur_dir_idx == 1:
                steps_possible = self.height - 1 - self.cur_pos[1]
                move = min(num, steps_possible)
                self.cur_pos[1] += move
                num -= move
                if num > 0:
                    self.cur_dir_idx = 2
            elif self.cur_dir_idx == 2:
                steps_possible = self.cur_pos[0]
                move = min(num, steps_possible)
                self.cur_pos[0] -= move
                num -= move
                if num > 0:
                    self.cur_dir_idx = 3
            elif self.cur_dir_idx == 3:
                steps_possible = self.cur_pos[1]
                move = min(num, steps_possible)
                self.cur_pos[1] -= move
                num -= move
                if num > 0:
                    self.cur_dir_idx = 0
        
        self.cur_dir = DIR_LIST[self.cur_dir_idx]

    def getPos(self) -> List[int]:
        return self.cur_pos

    def getDir(self) -> str:
        if self.cur_dir_idx == 0:
            return "East"
        elif self.cur_dir_idx == 1:
            return "North"
        elif self.cur_dir_idx == 2:
            return "West"
        else: # self.cur_dir_idx == 3
            return "South"
