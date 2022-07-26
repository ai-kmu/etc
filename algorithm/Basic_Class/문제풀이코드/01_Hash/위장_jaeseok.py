from collections import defaultdict
def solution(clothes):
    answer = 1
    # defaultdict를 사용하여 종류별 옷을 카운트함
    clothesdict = defaultdict(int)
    for i, j in clothes:
        # 옷의 종류별로 하나씩 더함
        clothesdict[j] += 1
    for i in clothesdict.values():
        # 옷 종류별로 가능한 가지수는 (종류별 옷의 개수 + 1)을 곱해주면 됨
        answer *= (i + 1)
    # 옷을 아무것도 입지 않는 선택지는 없으로 -1을 빼서 return
    return answer - 1
