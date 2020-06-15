# 다른 사람 풀이 참고
def solution(number, k):
    answer = ''

    stack = []
    for (i, num) in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break
        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    answer = ''.join(stack)
    return answer

number_1 = '1924'
number_2 = '1231234'
number_3 = '4177252841'

k_1 = 2
k_2 = 3
k_3 = 4

print(solution(number_1, k_1))
print()
print(solution(number_2, k_2))
print()
print(solution(number_3, k_3))


# from itertools import combinations
#
# # 내 풀이 ... combinations모듈을 활용하여 조합 구해서 최댓값 구하기
# def solution(number, k):
#     answer = ''
#
#     # '1924' -> [1, 9, 2, 4]
#     number_lst = [one for one in number]
#
#     # number 문자열에서 k개 제거한 조합 가지 수 구하기
#     remove_k_cnt = list(combinations(number_lst, len(number) - k))
#
#     # 가장 큰 값 저장 변수
#     max_cost = 0
#
#     # 각 경우 대해 정수 저장 리스트
#     case_lst = []
#
#     # 조합 경우의 수 반복 ('1', '9'), ...
#     for case in remove_k_cnt:
#         # '1', '9' -> '19'
#         case_str_sum = ''
#         for k_one in case:
#             case_str_sum += k_one
#         case_lst.append(int(case_str_sum))
#     max_cost = max(case_lst)
#
#     answer = str(max_cost)
#     return answer
