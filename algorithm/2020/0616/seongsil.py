def solution(number, k):
    answer = list()
    for i, num in enumerate(number): 
        while answer and num > answer[-1] and k > 0: # 앞의 수들과 비교하여 앞의 수들보다 현재 수가 크면 앞 수 제거
            answer.pop()
            k-=1
        if k == 0:  # k가 0일 경우 뒤에 숫자 이어붙임
            answer.extend(number[i:])
            break

        answer.append(num)
    answer = answer if k==0 else answer[:-k]  # ex) 9,9,9,9 같은 수 나올 경우 예외처리
        
    return "".join(answer)
