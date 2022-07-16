import sys

# 긴 값을 data로 짧은값을 filter로 두고 filter로 data를 순회하면서 최댓값을 구하는 방식

# 입력받기
a = input()
N, M, K= list(map(int,a.split()))

pattern1 = input()
pattern1 = list(map(int,pattern1.split()))

pattern2 = input()
pattern2 = list(map(int,pattern2.split()))

menu_filter, filter_len = [pattern2, M] if N > M else [pattern1, N]
data, data_len = [pattern1, N] if N > M else [pattern2, M]

# 값 초기화
whole_length = data_len + 2*(filter_len-1)
max_pattern = 0
cur_position = 0

# 탐색
for i in range(whole_length):
    # filter 설정
    if i <= filter_len:
        fltr = menu_filter[-(i+1):]
    elif whole_length-i <= filter_len:
        cur_position += 1
        fltr = fltr[:-1]
    else:
        fltr = menu_filter
        cur_position += 1
    
    # 겹치는 pattern의 최대길이 구하기
    pattern = 0
    for a, b in zip(fltr, data[cur_position:cur_position+len(fltr)]):
        if a == b: 
            pattern += 1
            max_pattern = max(max_pattern, pattern)
        else:
            pattern = 0

print(max_pattern)
