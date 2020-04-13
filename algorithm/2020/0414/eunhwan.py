def solution(food_times, k):
    times = {}
    for idx, time in enumerate(food_times):
        if time in times:
            times[time].append(idx)
        else:
            times[time] = [idx]

    len_foods = len(food_times)
    cycle = 0
    for time in sorted(times):
        """
        [1, 2, 3]
        K -= T[0] * len(3)
        K -= (T[1] - T[0]) * len(2)
        ...
        오름차순 정렬을 하여 삭제해나간다.
        """
        if k - (len_foods * (time - cycle)) >= 0:
            k -= len_foods * (time - cycle)
            len_foods -= len(times[time])
            cycle += time - cycle
        else:
            k %= len_foods
            for i in times:
                if i >= time:
                    idx = times[i][0]
                    break
            # 원래 위치로다시 복구시키기
            for i in range(idx, len(food_times)):
                if food_times[i] >= time:
                    if k == 0:
                        return i + 1
                    else: k -= 1
    return -1
