def binary_search(potions, spell, start, end, success):
    
    if start > end:
        # 탐색 범위가 역전되었을 때, 현재 위치가 탐색된 위치이므로 나머지 포션의 개수를 반환
        return len(potions) - start

    mid = (start + end) // 2

    if spells[i] * potions[mid] >= success:
        # 왼쪽 부분을 탐색
        return binary_search(potions, spell, start, mid - 1, success)
    else:
        # 오른쪽 부분을 탐색
        return binary_search(potions, spell, mid + 1, end, success)


result = []
potions.sort()  # potions 리스트를 정순으로 정렬

for i in range(len(spells)):
    start, end = 0, len(potions) - 1
    count = binary_search(potions, spells[i], start, end, success) #재귀 진행
    result.append(count)
  
return result
