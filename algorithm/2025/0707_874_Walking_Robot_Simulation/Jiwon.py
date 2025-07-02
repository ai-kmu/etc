class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 북동남서
        obstacles = set(map(tuple, obstacles))  # 장애물
        
        # 현재 로봇 위치: (0, 0), 방향: (0, 1)
        robot = (0, 0)
        dir_idx = 0
        ans = 0

        for command in commands:
            # 회전이 아닌 경우 전진
            if command > 0:
                for _ in range(command):
                    check = (robot[0] + dir[dir_idx][0], robot[1] + dir[dir_idx][1])
                    if check not in obstacles:
                        robot = check  # 장애물 없는 경우 위치 업데이트
                        ans = max(ans, robot[0] ** 2 + robot[1] ** 2)  # 거리 업데이트
                    # 장애물 마주친 경우 현재 명령 수행 중단
                    else:
                        break
            
                    
            # 회전인 경우 
            elif command == -2:  # 왼쪽 회전: 북-서 0-3
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # 오른쪽 회전: 북-동 0-1
                dir_idx = (dir_idx + 1) % 4

        return ans
