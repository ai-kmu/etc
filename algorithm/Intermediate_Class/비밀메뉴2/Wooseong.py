# 이분탐색 이용
# 시간 초과...

import sys

N, M, K = map(int, sys.stdin.readline().split())

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

# M을 긴 걸로 만들기
if N > M:
    first, second = second, first
    N, M = M, N

# first[sp:ep]가 second[start:]에 있는지 확인하는 재귀 함수
# 있으면 True 없으면 False
def compare(sp, ep, start):
    # 애초에 길이가 더 짧으면 있을 수 없다
    if (M - start) < (N - ep):
        return False
    
    i = 0
    stack = 0
    # 하나씩 비교하면서
    for ind in range(start, M):
        # 똑같으면 진행
        if second[ind] == first[sp + i]:
            stack += 1
            i += 1
            # 다 똑같으면 True
            if (N - ep) == stack:
                return True
        # 다른 게 있으면 재귀
        else:
            # 시작점은 first[sp:ep]의 첫 요소의 second에서 또 다른 위치
            second_part = second[start+1:]
            if first[sp] in second_part:
                idx = second_part.index(first[sp])
                return compare(sp, ep, start + 1)
            
            # 첫 요소가 더 이상 없으면 False
            return False

# 메인 함수
def main():
    # first 자르는 이분 탐색 *주석1
    for ep in range(N - 1):
        for sp in range(ep + 1):
            # 시작점은 first[sp:ep]의 첫 요소의 second에서의 위치
            if first[sp] in second:
                idx = second.index(first[sp])
                # 있으면 해당 길이 반환
                if compare(sp, ep, idx):
                    return N - ep
    
    # 한 개 짜리는 요소가 있나 없나로 탐색
    for elem in first:
        if elem in second:
            return 1

    return 0

# 실행
print(main())


''' 주석1
first[i:len-(j-i)]
j = 0 / i = 0 to 0 
    first[0:len]
j = 1 / i = 0 to 1
    first[0:len-1], first[1:len]
j = 2 / i = 0 to 2
    first[0:len-2], first[1:len-1], first[2:len]
...
j = len-1 / i = 0 to len-1
    first[0:len-(len-1-0)], ..., first[len-1:len]
'''
