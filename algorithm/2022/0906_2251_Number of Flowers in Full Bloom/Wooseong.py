class Solution:
    def fullBloomFlowers(self, flowers, persons):
        # 각 날의 시작 / 끝에 피는 꽃 수 저장
        blooms_at_day = defaultdict(int)
        for start, end in flowers:
            blooms_at_day[start] += 1
            blooms_at_day[end + 1] -= 1
        days = sorted(blooms_at_day.keys())
        # print(days)
        # >>> [1, 3, 4, 7, 8, 9, 13, 14]
        
        prev = 0
        for i in days:
            blooms_at_day[i] += prev
            prev = blooms_at_day[i]
        # print(blooms_at_day)
        # >>> {1:1, 3:2, 4:3, 7:2, 8:1, 9:2, 13:1, 14:0}
        
        
        # days에서 person이 방문한 시점의
        # 왼쪽 혹은 일치하는 값을 갖고와서  --> bisect_left
        # 그 값(i)에 해당하는 blooms_at_day를 확인하면
        # person이 볼 수 있는 꽃의 수이다.
        #   1. 왼쪽을 본다: 모든 경우가 아닐 때는 blooms_at_day[days[i-1]]
        #   2. 일치하는 값: blooms_at_day[days[i]]
        # 예외
        #   3. 다 지고 나서 온 경우 = days의 최댓값보다 큼
        #       -> bisect_left가 days의 길이를 return하게 된다
        #       -> 그 경우 0을 추가
        #   4. 피기도 전에 온 경우 = 0
        #       -> 일치해서 0을 뱉었을 수도 있다. 따라서 2번 먼저 처리해야됨
        #       -> 역시 0을 추가
        answer = []
        n = len(days)
        for person in persons:
            i = bisect_left(days, person)
            # 3번
            if i == n:
                answer.append(0)
            # 2번 
            elif days[i] == person:
                answer.append(blooms_at_day[days[i]])
            # 4번
            elif i == 0:
                answer.append(0)
            # 1번
            else:
                answer.append(blooms_at_day[days[i-1]])
        
        return answer
