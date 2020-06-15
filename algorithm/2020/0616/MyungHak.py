"""
    자기보다 작은수가 먼저 와있는 경우 그 수를 지우고 그 자리를 차지한다.
"""

def solution(number, k):
    answer_length = 1
    answer = number[0]  # 우선 answer에 제일 첫번째 수를 넣어 놓는다.
    total_length = len(number)     
    maximum_answer_length = total_length - k  # 허용 가능한 최대 범위 지정
    for i in range (1, total_length):
        if number[i] > answer[-1]:
            while(0 < answer_length and number[i] > answer[answer_length-1]):  # 자기보다 큰 수가 나올때 까지 계속 넣어져 있는 수를 지워나간다
                if k == 0: # 그러다 k가 0이되면 나머지 수를 자 출력한다.
                    return [answer[:answer_length] + number[i:]][:maximum_answer_length][0] 
                answer_length -=1
                k-=1
            answer = answer[:answer_length] + number[i]
            answer_length +=1
        elif answer_length <= maximum_answer_length:  # 현재 자기보다 큰수가 앞에 와있는경우 그냥 이어 붙인다. 단 maximum은 넘지 않도록
            answer += number[i]
            answer_length +=1
    return answer[:maximum_answer_length]
