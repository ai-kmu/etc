class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # 공의 개수 및 현재 공의 인덱스
        balls_num = len(grid[0])
        ball_list = [i for i in range(balls_num)]
        
        # 만약 생성된 공의 개수가 1개일 경우 -1 반환
        # [[1]] 이나 [[-1]] 모두 -1을 반환
        if len(ball_list) == 1: return [-1]
    
        for i in grid:
            for idx, j in enumerate(ball_list):
                # 현재 공이 가리키는 값이 -1이 아닌 경우에만 루프를 돔
                if j != -1:
                    # 현재 0번째일 때 공이 걸릴 경우 -1로 바꿔줌
                    if j == 0 and (i[0] == -1 or (i[0] == 1 and i[1] == -1)):
                        ball_list[idx] = -1
                        continue
                    # 현재 공이 행의 끝에 있을 때 공이 걸리면 -1로 바꿔줌
                    elif j == (balls_num-1) and(i[-1] == 1 or (i[-1] == -1 and i[-2] == 1)):
                        ball_list[idx] = -1
                        continue
                    # 공이 0이나 끝이 아닐 때 루프
                    elif j != 0 or j != (balls_num-1):
                        # 공이 걸릴 때 -1로 바꿔줌
                        if (i[j-1] == 1 and i[j] == -1) or (i[j] == 1 and i[j+1] == -1):
                            ball_list[idx] = -1
                            continue
                        # 공이 걸리지 않을 경우 현재 grid의 값을 더해줌
                        else:
                            ball_list[idx] += i[j]
                            continue
                    # 만약 공이 -1이 아닐 경우 grid값을 더해줌
                    # 여기서 더해줄 경우는 공이 0번째나 끝번째에 있었는데 걸리지 않는 경우
                    else : ball_list[idx] += i[j]    
            
        return ball_list
