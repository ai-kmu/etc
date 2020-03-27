def solution(arrangement):
    answer = 0

    # 리스트로 괄호 하나하나에 대해 연산
    arrange_list = list(arrangement)
    tmp = list()

    # 자르기 전과 후의 막대의 개수 저장하는 변수
    cutting_before = 0
    cutting_after = 0

    # list 길이만큼 돌면서 맨 앞의 요소에 따라 막대의 개수 판단
    for bracket in range(len(arrange_list)):
        first = arrange_list.pop(0)
        if first == '(':
            cutting_before += 1
            cutting_after += 1
        else:
            if tmp[-1] == '(':
                cutting_before -= 1
                cutting_after -= 1
                cutting_after += cutting_before
            else:
                cutting_before -= 1
        tmp.append(first)
    answer = cutting_after
    return answer

arrangement_1 = '()(((()())(())()))(())'
print(solution(arrangement_1))