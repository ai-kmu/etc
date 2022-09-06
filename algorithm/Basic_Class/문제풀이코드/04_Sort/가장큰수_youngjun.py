# 풀이 실패 ㅠㅠㅠ
# 테스트케이스는 다 맞으나 실제로 돌렸을때 오류 ㅠ

def solution(numbers):
    # numbers들의 숫자 원소들을 문자로 변환하여 일차적으로 정렬함
    str_numbers = []
    for num in numbers:
        str_numbers.append(str(num))

    str_numbers.sort(reverse = True)
    
    # 결국 앞자리가 다른 원소들은 우선적으로 정렬
    # 그러나 앞자리가 같은 원소들끼리의 정렬이 문제임
    # for문으로 순환하면서
    for i in range(len(str_numbers) - 1):
        # i번째와 i + 1번째 원소가 앞자리가 같을 경우, 
        if str_numbers[i][0] == str_numbers[i + 1][0]:
            # 두 문자열을 합한 것을 int했을 때, 순서를 바꾼 것이 안바꾼 것보다 더 크면
            if int(str_numbers[i] + str_numbers[i + 1]) < int(str_numbers[i + 1] + str_numbers[i]):
                # 순서를 바꿔준다.
                str_numbers[i], str_numbers[i + 1] = str_numbers[i + 1], str_numbers[i]
                
    # 만약 [0,0,0,0] 등 0으로만 이루어진 문자열일 경우
    if str_numbers[0] == '0':
        answer = '0'
    else:
        answer = "".join(str_numbers)
    
    return answer
