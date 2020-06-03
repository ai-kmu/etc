#백준_And the Winner Is... Ourselves!
#10:30~11:45

def solution():

    answer=0
    info=[]

    for i in range(0,11):
        input_time, input_incorrect_verdicts = map(int, input().split())  # 문제 푸는데 걸린 시간, 패널티
        info.append((input_time,input_incorrect_verdicts))

    info.sort(key=lambda t: t[0])

    time=0
    penalty=0
    for i in info:
        time+=i[0]
        penalty+=time+20*i[1]
    answer=penalty

    return answer

if __name__ == '__main__':
    print(solution())