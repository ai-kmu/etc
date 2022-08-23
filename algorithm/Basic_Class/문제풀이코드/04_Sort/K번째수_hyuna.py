def solution(array, commands):
    answer = []
    
    for command in commands:
        # i번째 숫자부터 j번째 숫자까지 자르기 
        sub = array[command[0]-1:command[1]]
        # 오름차순으로 정렬하기
        sub.sort()
        # 정렬한 배열에서 k번째 수 뽑아서 answer 리스트에 추가하기 
        answer.append(sub[command[2]-1])
        
    return answer
