# 단순히 부분배열들을 전부 생성해서 구한다.
def solution(array, commands):
    answer = []
    for cmd in commands:
        tmp = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(tmp[cmd[2]-1])
    return answer
