def max_next_height(max_answer, triangle, current_h):
    next_h = current_h +1
    # 존재하지않는 것을 막기 위해 초기화
    max_answer.append([0 for i in range(len(triangle[next_h]))])
    for i in range(len(triangle[current_h])):
            max_answer[next_h][i] = max(max_answer[next_h][i], max_answer[current_h][i]+triangle[next_h][i])
            max_answer[next_h][i+1] = max(max_answer[next_h][i+1], max_answer[current_h][i]+triangle[next_h][i+1])
            
def solution(triangle):
    answer = 0
    height = len(triangle)
    max_answer = [[triangle[0][0]]]
    for h in range(height-1):
        max_next_height(max_answer, triangle, h)

    answer = max(max_answer[-1])
    return answer
