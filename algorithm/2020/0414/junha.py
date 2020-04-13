'''
(-1을 return하는 경우가 필요한지는 실험을 통해 알아보자.)
1. food_times를 sort한다.
2. cur_min = list[0]; cur_pos = 0; n = len(food_times);
3. while cur_min * n <= k :
   diff라는 개념! food_times간의 차이 <- 실수해서 초반 오답 해결: 손코딩한거 직접 예제 돌려보자. 
   k, cur_min과 cur_pos를 갱신
   cur_pos가 2001이면 -1 return하고 함수 종료
4. 위의 while이 break되면, cur_min의 값보다 같거나 큰 수들 중, (k)%n 번쨰 음식을 찾는다.
'''


def cur_next(lis, cur_min, cur_pos, n, l):
    for i in range(cur_pos+1, l):
        if cur_min < lis[i]:
            return lis[i], i
    return -1 , l+1

def fine_index(food_times, m, cur_min) : 
    for index, Value in enumerate(food_times):
        if cur_min <= Value :
            if m == 0:
                return index+1
            else :
                m -= 1

def solution(food_times, k):
    # 1
    lis = food_times[:]
    lis.sort()
    # 2
    cur_min = lis[0]
    diff = cur_min
    cur_pos = 0 # list 0부터 시작
    n = len(lis) # 남은 음식 수
    l = n # 처음 음식의 총 갯수
    # 3
    while diff*n <= k:
        k = k - diff*n
        temp, cur_pos = cur_next(lis, cur_min, cur_pos, n, l)
        if temp == -1 : return -1 # k가 충분히 커, 음식을 다 먹었을 경우.
        diff = temp - cur_min
        cur_min = temp
        n = l - cur_pos
        
    # 4
    cur_min = lis[cur_pos]
    answer = fine_index(food_times, k%n, cur_min)
    return answer
