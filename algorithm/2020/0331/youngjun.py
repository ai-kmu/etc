#백준 11047번(동전)
#5:25~6:20

def solution():
    answer = 0
    value_list_size, total_value = map(int, input().split()) #동전 가치 개수, 전체 동전 가치
    value_list=[] # 동전의 가치를 담을 리스트

    #동전 가치 담기
    for i in range(0, value_list_size):
        tmp=int(input())
        value_list.append(tmp)

    #동전 가치 오름차순으로 sort
    value_list.sort()

    #
    for i in reversed(range(value_list_size)):
        if total_value == 0: #동전 가치가 0일 경우
            break
        quotient=int(total_value/value_list[i]) # 동전 가치가 0이 아닐 경우, 몫 계산

        if quotient!=0: #몫이 0이 아닌 경우(현재 리스트의 동전 가치보다 남은 동전 가치가 더 크다는 의미 )
            total_value%=value_list[i] # 나머지를 구해서 남은 동전 가치를 다시 계산
            answer+=quotient # 몫을 더해서 사용된 동전 개수를 더해줌

    print(answer)

if __name__ == '__main__':
    solution()