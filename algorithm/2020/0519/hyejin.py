def solution(answers):
    answer = [0,0,0]
    one = [1,2,3,4,5]
    one_len = len(one)
    two = [2,1,2,3,2,4,2,5]
    two_len = len(two)
    three = [3,3,1,1,2,2,4,4,5,5]
    three_len = len(three)
    # answers 한번씩 돌면서 다 검사.
    for i,v in enumerate(answers):
        if one[i%one_len] == v: 
            answer[0] += 1
        if two[i%two_len] == v:
            answer[1] += 1
        if three[i%three_len] == v:
            answer[2] += 1
    
    # 최대로 가지는 값 찾아서 for문 돌면서 최대값 가지는 사람 추가하기
    max_value = max(answer)
    max_person = []
    for i,v in enumerate(answer):
        if max_value == v:
            max_person.append(i+1)
        
    return max_person
