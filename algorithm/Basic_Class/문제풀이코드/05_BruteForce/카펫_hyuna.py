def solution(brown, yellow):
    answer = []
    
    # 가능한 카펫의 노란색 부분의 height와 width를 먼저 구해주고 
    # 갈색 부분의 조건과도 적합한지 판단한다
    
    # 가로가 세로보다 길어야하기 때문에 for문을 돌때 큰 수부터 확인한다
    for w in range(yellow, 0, -1):
        # yellow가 w로 나누어 떨어질 경우
        if not yellow % w:
            # 세로 길이를 구해준다
            h = yellow // w
            # 구해준 가로 세로 길이의 사각형의 테두리가 갈색 부분과 일치 할 경우 답을 넣고 for을 빠져나온다
            if (2 * (w + h) + 4) == brown:
                answer = [w+2, h+2]
                break
                       
    return answer
