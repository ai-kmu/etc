def solution(f, k):
    if sum(f) <= k:
      return -1
    # 정렬된 food 리스트를 만든다.
    food = sorted(f)

    i = 0
    k -= food[i] * (len(food) - i)
    while k > 0 :
        i += 1
        k -= (food[i] - food[i-1]) * (len(food) - i)

    # 임시로 저장해놓는다.
    temp = food[i]
    while k < 0:
        temp -= 1
        k += len(food) - i

    # 원본 순서대로
    answer = 0
    for i, val in enumerate(f):
        if val > temp:
            if k <= 0:
              return i + 1
            else:
              k -= 1

    return answer
