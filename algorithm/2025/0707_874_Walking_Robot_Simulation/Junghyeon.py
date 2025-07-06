# 실패

class Solution(object):
    def robotSim(self, commands, obstacles):
        # (0, 90, 180, 270, 360)
        start_point = [0, 0]
        direction = 0

        result = []

        for c in commands:
            # change direction
            if c == -1:
                direction += 90
                if direction == 360:
                    direction = 0
                continue

            if c == -2:
                direction -= 90
                if direction == -90:
                    direction = 270
                continue
            
            # north
            if direction == 0:
                flag = True
                dst_point = start_point[1] + c
                for obs in obstacles:
                    if start_point[0] == obs[0] and start_point[1] < obs[1] < dst_point:
                        start_point[1] = obs[1] - 1
                        flag = False
                        # continue
                if flag:
                    start_point[1] = dst_point

            # east
            elif direction == 90:
                flag = True
                dst_point = start_point[0] + c
                for obs in obstacles:
                    if start_point[1] == obs[1] and start_point[0] < obs[0] < dst_point:
                        start_point[0] = obs[0] - 1
                        flag = False
                        # continue
                if flag:
                    start_point[0] = dst_point

            # south
            elif direction == 180:
                flag = True
                dst_point = start_point[1] - c
                for obs in obstacles:
                    if start_point[0] == obs[0] and start_point[1] < obs[1] < dst_point:
                        start_point[1] = obs[1] + 1
                        flag = False
                        # continue
                if flag:
                    start_point[1] = dst_point

            # west
            elif direction == 270:
                flag = True
                dst_point = start_point[0] - c
                for obs in obstacles:
                    if start_point[1] == obs[1] and start_point[0] < obs[0] < dst_point:
                        start_point[0] = obs[0] + 1
                        flag = False
                        # continue
                if flag:
                    start_point[0] = dst_point
            
            print(direction)
            print(start_point)

            result.append(start_point[0]**2 + start_point[1]**2)

        return max(result)
