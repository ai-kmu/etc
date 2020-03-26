def solution(arrangement):
    answer = 0
    arrange_list = list(arrangement)
    tmp = list()

    cutting_before = 0
    cutting_after = 0

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

arrange_1 = '()(((()())(())()))(())'
print(solution(arrange_1))