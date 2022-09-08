from itertools import permutations as pm

def solution(numbers):
    n = len(numbers)
    
    # 모든 숫자 쌍 반환
    cands = set()
    for i in range(1, n + 1):
        temp = [int(''.join(pair)) for pair in pm(numbers, i)]
        cands.update(temp)
        
        # max값은 어차피 다 뽑을 때 나옴 여기서만 확인
        if i == n:
            max_ = max(temp)
    
    # 에라토스테네스의 체
    check = [False] * 2 + [True] * (max_ - 1)
    primes = []
    for i in range(2, max_ + 1):
        if check[i]:
            primes.append(i)
            for j in range(2 * i, max_ + 1, i):
                check[j] = False
    
    # 소수 개수 세기
    # int에 Bool을 더하면 True = 1, False = 0으로 자동 변환
    answer = 0
    for cand in cands:
        answer += (cand in primes)
        
    return answer
