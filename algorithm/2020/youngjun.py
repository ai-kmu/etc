#백준 11047번(동전)
#5:25~6:20

def solution():
    answer = 0
    value_list_size, total_value = map(int, input().split())
    value_list=[]

    for i in range(0, value_list_size):
        tmp=int(input())
        value_list.append(tmp)

    value_list.sort()

    for i in reversed(range(value_list_size)):
        if total_value == 0:
            break
        quotient=int(total_value/value_list[i])
        if quotient!=0: #몫이 0이 아닌 경우(나눌 수 있는 돈)
            total_value%=value_list[i]
            answer+=quotient

    print(answer)

if __name__ == '__main__':
    solution()