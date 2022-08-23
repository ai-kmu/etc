
def solution(array, commands):
    answer = []
    temp = []

    # 돌면서 시작 끝 타겟 해야할거 찾고
    # temp 에 시작 끝 정렬해서 넣어주고 타겟값 answer에 추가
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        target = commands[i][-1]
        temp.append(sorted(array[start-1:end]))
        answer.append(temp[i][target-1])
        
    return answer
