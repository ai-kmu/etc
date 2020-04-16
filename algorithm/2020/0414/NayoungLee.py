def solution(food_times, k):
    answer = 0
    first = 0
    orin_num = 0
    check = -1 #num2와 같은 수를 찾는 변수
    #먹는시간의 순서를 기억하는 새로운 배열 생성
    new_f_t = []
    for i in range(len(food_times)):
        new_f_t.append([food_times[i],i+1])
    food_times.sort()

    #k와 시간 비교
    while True:
        first += food_times[0] #흘러간 시간 누적
        num = food_times[0] * len(food_times)
        
        #k에서 남은 시간 줄이기
        if k > num:
            k -= num
        elif k == num:
            for u in range(len(new_f_t)):
                if new_f_t[u][0] < orin_num:
                    del new_f_t[u][0]
            answer = new_f_t[0][1]
            break
        else:
            num2 = k % len(food_times)
            for j in range(len(new_f_t)):
                if new_f_t[j][0] >= orin_num:
                    check += 1
                    if check == num2:
                        break
                    continue
                check += 1
                num2 += 1
            answer = new_f_t[check][1]
            break
        
        del food_times[0] #0번째 데이터 삭제
        #남은 음식이 없을 때 -1 반환
        if not food_times:
            answer = -1
            break
        orin_num = food_times[0]
        food_times[0] -= first #0번째만 누적된 흘러간 시간을 빼준다.

    return answer
