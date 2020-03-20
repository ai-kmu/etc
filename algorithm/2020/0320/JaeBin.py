# 12. 프린터

def solution(priorities, location):
    answer = 0
    first = priorities[0]
    big = 0
    stack = []

    for i in range(len(priorities)):
        stack.append([priorities[i], i])
        if first < priorities[i]:
            big = stack[i]
    # big = max(stack[len(priorities)])
    # print('big : ', big)

    while big[0] != first:
        cost = stack.pop(0)
        stack.append(cost)
        first = stack[0][0]

    # print('stack : ', stack)
    answer_lst = [i+1 for i in range(len(stack)) if stack[i][1] == location]
    answer = answer_lst.pop()
    return answer

priorities_1 = [2, 1, 3, 2]
location_1 = 2
priorities_2 = [1, 1, 9, 1, 1, 1]
location_2 = 0
print(solution(priorities_1, location_1))
print()
print(solution(priorities_2, location_2))

# 내 풀이 index 처리가 완벽하게 되지 않아 skip
# def solution(priorities, location):
#     answer = 0
#     first = priorities[0]
#     move = 0
#     big = 0
#
#     for idx in range(len(priorities)):
#         if first < priorities[idx]:
#             big = priorities[idx]
#     # print('big : ', big)
#
#     while first != big:
#         cost = priorities.pop(0)
#         priorities.append(cost)
#         first = priorities[0]
#         move += 1
#
#     print(priorities)
#     answer = priorities.index(priorities[-move])
#     return answer


# 다른 사람 풀이
def solution(priorities, location):
    pi_list = [(p, i) for i, p in enumerate(priorities)]
    print('pi_list : ', pi_list)
    waiting_q = []
    max_p = 0

    while pi_list:
        pi = pi_list.pop(0)
        print('pi : ', pi)
        priority = pi[0]
        print('priority : ', priority)
        p_list = [priority for priority, idx in pi_list]
        if p_list:
            max_p = max(p_list)

        if priority >= max_p:
            waiting_q.append(pi)
        else:
            pi_list.append(pi)

    for i, item in enumerate(waiting_q):
        if item[1] == location:
            return i+1