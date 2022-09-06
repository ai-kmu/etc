# 타임에러 permutation 에서 생기는거 같습니다
from itertools import permutations

def solution(numbers):
    # 순열만들고
    # 맥스 리턴
    permute = list(permutations(numbers,len(numbers)))
    list_permute = [''.join(map(str,i)) for i in permute]   
    answer = max(list_permute)
    
    return answer
