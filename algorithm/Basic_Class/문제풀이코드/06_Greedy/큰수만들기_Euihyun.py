# 4문제 빼고 다 시간초과 납니다.
from itertools import combinations

def solution(number, k):
    # k 개 빼고  남은 숫자들로 조합생성
    num = list(combinations(number,len(number)-k))
    # ('1','9') 를 19로 만들고
    com = [''.join(map(str,i)) for i in num]
    # 해당 리스트에서 최대값 출력
    return max(com)

