def max_next_height(max_answer, triangle, current_h):
    next_h = current_h +1
    # 존재하지않는 것을 막기 위해 초기화
    max_answer.append([0 for i in range(len(triangle[next_h]))])
    
    # 현재 height로 다음 height 값을 계산 / 전에 계산된 값이 있을수도 있기 떄문에 비교해서 max값을 넣음
    for i in range(len(triangle[current_h])):
            max_answer[next_h][i] = max(max_answer[next_h][i], max_answer[current_h][i]+triangle[next_h][i])
            max_answer[next_h][i+1] = max(max_answer[next_h][i+1], max_answer[current_h][i]+triangle[next_h][i+1])
            
def solution(triangle):
    answer = 0
    height = len(triangle)
    max_answer = [[triangle[0][0]]]
    # 하나하나씩 다 계산하기
    for h in range(height-1):
        max_next_height(max_answer, triangle, h)

    answer = max(max_answer[-1])
    return answer
