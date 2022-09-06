def solution(array, commands):
    answer = []
    
    # 문제 설명에서 설명해준 것과 같은 순서로 진행
    # 1. 인덱스를 이용해 리스트 슬라이싱
    # 2. 슬라이싱한 리스트를 정렬
    # 3. 그 중 k번째 수 정답 리스트에 넣기
    for i in commands:
        cnt = 1
        for j in sorted(array[i[0]-1:i[1]]):
            if cnt == i[2]:
                answer.append(j)
                break
            cnt += 1
        else : answer.append(-1)
    return answer
