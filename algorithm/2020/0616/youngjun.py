number="4177252841"
k=4

def solution(number, k):
    answer = ''

    #수를 저장할 리스트
    num_collected = []

    for idx, val in enumerate(number):
        while num_collected and num_collected[-1] < val and k > 0: # collected에 값이 들어있고, 마지막 값이 현재 val 값보다 작고, k가 0보다 큰 경우
            num_collected.pop() # collected에서 마지막 숫자 빼줌
            k -= 1 # 숫자 pop 할때마다 k를 1개씩 빼줌

        if k == 0: # 만약 k가 0이 되면
            num_collected += number[idx:] # 남아있는 number collected 리스트에 모두 추가
            break

        num_collected.append(val) # 마지막 값이 현재 val 값보다 크고, k가 0보다 큰 경우

    num_collected = num_collected[:-k] if k > 0 else num_collected 
    answer = "".join(num_collected)

    return answer

if __name__ == '__main__':
    print(solution(number,k))

#시간초과 났던 풀이(10번문제)
# def solution(number, k):
#     answer = ''
#
#     # 내림차순으로 sort
#     number_length= len(number)
#     to_select_number=number_length-k
#
#     max_number_list=list()
#
#     end_index=number_length-to_select_number
#     max_number ="0"
#
#     idx=0
#     while to_select_number!=0:
#
#         if number[idx]>max_number:
#             max_number=number[idx]
#             max_number_idx=idx
#
#         if idx==end_index:
#             # max_number_list.append(max_number)
#             answer+=max_number
#             to_select_number -= 1
#
#             idx=max_number_idx
#             end_index =max_number_idx+(number_length-max_number_idx-1)-to_select_number+1
#
#             max_number = "0"
#
#         idx+=1
#
#     # answer=''.join(max_number_list)
#
#     return answer
#
#
# if __name__ == '__main__':
#     print(solution(number,k))